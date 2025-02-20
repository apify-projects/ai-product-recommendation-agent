## Python LangGraph template

A template for [LangGraph](https://www.langchain.com/langgraph) projects in Python for building AI agents with [Apify Actors](https://apify.com/actors). The template provides a basic structure and an example [LangGraph](https://www.langchain.com/langgraph) [ReAct agent](https://react-lm.github.io/) that calls [Actors](https://apify.com/actors) as tools in a workflow.

## How it works

A [ReAct agent](https://react-lm.github.io/) is created and given a set of tools to accomplish a task. The agent receives a query from the user and decides which tools to use and in what order to complete the task. In this case, the agent is provided with an [Instagram Scraper Actor](https://apify.com/apify/instagram-scraper) to scrape Instagram profile posts and a calculator tool to sum a list of numbers to calculate the total number of likes and comments. The agent is configured to also output structured data, which is pushed to the dataset, while textual output is stored in the key-value store as a `response.txt` file.

## How to use

Add or modify the agent tools in the `src/tools.py` file, and make sure to include new tools in the agent tools list in `src/main.py`. Additionally, you can update the agent system prompt in `src/main.py`. For more information, refer to the [LangGraph ReAct agent documentation](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent-system-prompt/) and the [LangChain tools documentation](https://python.langchain.com/docs/concepts/tools/).

For a more advanced multi-agent example, see the [Finance Monitoring Agent actor](https://github.com/apify/actor-finance-monitoring-agent) or visit the [LangGraph documentation](https://langchain-ai.github.io/langgraph/concepts/multi_agent/).

## Included features

- **[Apify SDK](https://docs.apify.com/sdk/python/)** for Python - a toolkit for building Apify [Actors](https://apify.com/actors) and scrapers in Python
- **[Input schema](https://docs.apify.com/platform/actors/development/input-schema)** - define and easily validate a schema for your Actor's input
- **[Dataset](https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-datasets)** - store structured data where each object stored has the same attributes
- **[Key-value store](https://docs.apify.com/platform/storage/key-value-store)** - store any kind of data, such as JSON documents, images, or text files

## Resources

- [What are AI agents?](https://blog.apify.com/what-are-ai-agents/)
- [Python tutorials in Academy](https://docs.apify.com/academy/python)
- [Apify Python SDK documentation](https://docs.apify.com/sdk/python/)
- [LangChain documentation](https://python.langchain.com/docs/introduction/)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [Integration with Make, GitHub, Zapier, Google Drive, and other apps](https://apify.com/integrations)


## Getting started

For complete information [see this article](https://docs.apify.com/platform/actors/development#build-actor-locally). To run the actor use the following command:

```bash
apify run
```

## Deploy to Apify

### Connect Git repository to Apify

If you've created a Git repository for the project, you can easily connect to Apify:

1. Go to [Actor creation page](https://console.apify.com/actors/new)
2. Click on **Link Git Repository** button

### Push project on your local machine to Apify

You can also deploy the project on your local machine to Apify without the need for the Git repository.

1. Log in to Apify. You will need to provide your [Apify API Token](https://console.apify.com/account/integrations) to complete this action.

    ```bash
    apify login
    ```

2. Deploy your Actor. This command will deploy and build the Actor on the Apify Platform. You can find your newly created Actor under [Actors -> My Actors](https://console.apify.com/actors?tab=my).

    ```bash
    apify push
    ```

## Documentation reference

To learn more about Apify and Actors, take a look at the following resources:

- [Apify SDK for JavaScript documentation](https://docs.apify.com/sdk/js)
- [Apify SDK for Python documentation](https://docs.apify.com/sdk/python)
- [Apify Platform documentation](https://docs.apify.com/platform)
- [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)
