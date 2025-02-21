from apify import Actor
from langchain_core.messages import ToolMessage

from src.models import AgentStructuredOutput


def log_state(state: dict) -> None:
    """Logs the state of the graph.

    Uses the `Actor.log.debug` method to log the state of the graph.

    Args:
        state (dict): The state of the graph.
    """
    message = state['messages'][-1]
    # Traverse all tool messages and print them
    # if multiple tools are called in parallel
    if isinstance(message, ToolMessage):
        # Until the analyst message with tool_calls
        for _message in state['messages'][::-1]:
            if hasattr(_message, 'tool_calls'):
                break
            Actor.log.debug('-------- Tool Result --------')
            Actor.log.debug('Tool: %s', _message.name)
            Actor.log.debug('Result: %s', _message.content)

    Actor.log.debug('-------- Message --------')
    Actor.log.debug('Message: %s', message)

    # Print all tool calls
    if hasattr(message, 'tool_calls'):
        for tool_call in getattr(message, 'tool_calls', []):
            Actor.log.debug('-------- Tool Call --------')
            Actor.log.debug('Tool: %s', tool_call['name'])
            Actor.log.debug('Args: %s', tool_call['args'])

def transform_output(response: AgentStructuredOutput | None, last_message: str):
    """Transforms the structured output into a list of dictionaries.

    We use this transformation before pushing to the dataset.

    Args:
        response (AgentStructuredOutput | None): The structured output from the ReAct agent.
        last_message (str): The last message from the ReAct agent.
    """
    if response is None:
        return [{'response': last_message}]
    return [
        {
            **rp.model_dump(include=['title', 'brand', 'stars', 'description', 'price', 'url', 'reviewSummary']),
            'response': last_message,
        }
        for rp in response.recommended_products
    ]

def get_html(markdown_response: str) -> str:
    """Wraps the markdown response in a HTML with some styles.

    We use the HTML as a final output shown to the user.

    Args:
        markdown_response (str): The markdown response to wrap.

    Returns:
        str: The HTML response.
    """
    css = '''
        <style>
            @import 'https://fonts.googleapis.com/css?family=Open+Sans';

            * {
                -webkit-box-sizing: border-box;
                box-sizing: border-box;
            }

            body {
                font-family: 'Open Sans', sans-serif;
                line-height: 1.75em;
                font-size: 16px;
                background-color: #222;
                color: #aaa;
            }

            .simple-container {
                max-width: 60%;
                margin: 0 auto;
                padding-top: 70px;
                padding-bottom: 20px;
            }

            p {
                font-size: 16px;
            }

            h1 {
                font-size: 30px;
                line-height: 34px;
            }

            h2 {
                font-size: 20px;
                line-height: 25px;
            }

            h3 {
                font-size: 16px;
                line-height: 27px;
                padding-top: 15px;
                padding-bottom: 15px;
                border-bottom: 1px solid #D8D8D8;
                border-top: 1px solid #D8D8D8;
            }

            hr {
                height: 1px;
                background-color: #d8d8d8;
                border: none;
                width: 100%;
                margin: 0px;
            }

            a[href] {
                color: #1e8ad6;
            }

            a[href]:hover {
                color: #3ba0e6;
            }

            img {
                max-width: 100%;
            }

            li {
                line-height: 1.5em;
            }

            @media (min-width: 1921px) {
                body {
                    font-size: 18px;
                }
            }
        </style>
        '''
    html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Recommendation</title>
            {css}
        </head>
        <body>
            <div class="simple-container">
                <h1>Recommendation</h1>
                <md-block>{markdown_response}</md-block>
            </div>
            <script type="module" src="https://md-block.verou.me/md-block.js"></script>
        </body>
        </html>
        '''
    return html