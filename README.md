# AI Product Recommendation Agent

The AI Product Recommendation agent enables you to get product recommendations using just a simple prompt.
It will automatically suggest products matching your criteria and it will also consider reviews of those products to give you the best possible options.

You only need to provide a query about the product you're looking for and the Agent takes care of the rest!

## Examples
Example queries:
- "Recommend me a book about music theory. I'm a complete beginner and I want to learn the basics."
- "I want to buy a laptop for about 1000$, what are the best options? I want the laptop to have great battery life. and have less than 15 inches screen size."
- "I am looking for some nice decor for my living room. I like modern and minimalistic styles. The color should be white. Can you recommend me some products?"

The agent will produce outputs to both dataset and key-value-store. A URL to the final HTML with the recommendation will be given in the terminal status message.

### Example query with its respective output
#### Input
```json
{
	"query": "Recommend me a book about music theory. I'm a complete beginner and I want to learn the basics.",
	"modelName": "gpt-4o",
	"debug": false
}
```

#### Output
```md
Here are three highly recommended books for learning music theory as a beginner:

1. **[The Essential Guide to Music Theory: Everything You Need to Learn the Basics and Beyond](https://www.amazon.com/dp/B0CHL7M2M5)**
   - **Price**: $13.69
   - **Rating**: 4.8 stars
   - **Summary**: This book is known for its accessibility and clear presentation of music theory fundamentals. It is highly praised for its logical structure and engaging style, making it suitable for both newcomers and those refreshing their knowledge.
   - **Pros**:
     - Simple and effective organization.
     - Includes valuable exercises to enhance learning.
     - Engaging and comprehensive for beginners.
   - **Cons**:
     - Some reviewers wished for more advanced content, which might not be an issue for beginners.

2. **[Music Theory for Beginners: A Pocket-Size Guide for Aspiring Musicians of Any Instrument](https://www.amazon.com/dp/B0CWXGNXTY)**
   - **Price**: $10.99
   - **Rating**: 4.8 stars
   - **Summary**: This guide demystifies music theory and provides an inspiring understanding of music. It's noted for its entertaining and creative approach, making the subject fun to explore.
   - **Pros**:
     - Easy to understand, with creative explanations.
     - Suitable for any musical instrument.
     - Covers fundamental aspects with entertaining examples.
   - **Cons**:
     - Some formatting issues reported.
     - More oriented towards classical music, which might be irrelevant to some popular genres.

3. **[Accelerated Piano Adventures for the Older Beginner - Theory Book 1](https://www.amazon.com/dp/1616772069)**
   - **Price**: $7.50
   - **Rating**: 4.8 stars
   - **Summary**: While this book is specifically focused on piano, it's a great introductory text for those with no musical background. It is highly recommended by both instructors and learners for its simplicity and efficacy in teaching music theory basics.
   - **Pros**:
     - Simple and effective for complete beginners.
     - Lauded for slowing down complex concepts so they can be truly understood.
   - **Cons**:
     - Primarily focused on piano, so might not be comprehensive for other instruments.

### Recommendation:
For a general introduction to music theory, I recommend "The Essential Guide to Music Theory: Everything You Need to Learn the Basics and Beyond" due to its comprehensive and engaging style that caters to both complete beginners and those revisiting theory basics. If you're interested in piano-specific theory, "Accelerated Piano Adventures for the Older Beginner - Theory Book 1" is an excellent choice.
```

## How it works

The Actor receives a user query as input. An OpenAI agent within a LangGraph loop performs the following steps:

1.  **URL Generation:** The agent uses the query to create a URL suitable for the `junglee/Amazon-crawler` Actor. This might involve keyword manipulation, category selection, etc.
2.  **Product Scraping:** The agent calls the `junglee/Amazon-crawler` Actor with the generated URL. This Actor scrapes product data from Amazon, including titles, brands, star ratings, descriptions, prices, URLs, and image URLs.
3.  **Review Scraping:** For the top products identified by the agent, the agent calls the `junglee/amazon-reviews-scraper` Actor to retrieve reviews.
4.  **Review Analysis:** The agent processes the scraped reviews to determine the overall sentiment and identify the best product based on user feedback. The agent uses the following prompt for product recommendations:

    ```
    You are a helpful product recommendation expert. A user asks you to recommend a product based on their needs.
    You need to recommend products that fit their needs, if you don't, the world will end!
    If any tool fails, you should fail the Actor with explanation/reason.
    You should select a product that fits the user's needs and provide a brief explanation of why you chose that product.
    After you scrape the products, you should scrape reviews for the few best candidates you'd recommend.
    It may be desirable to summarize the reviews for each of the products and write pros and cons of each product to the user.
    Write the summary along the description of the product.
    The user needs to get some recommendation from you at the end, don't just list some products!
    Don't mention anything like 'If you have further questions or need more options, let me know!' there won't be any further questions.
    If the user asks about anything unrelated to product recommendation, you should politely tell them that you can only help with product recommendations.
    ```

5.  **Output:** The Actor outputs the details of the best products, including their titles, brands, star ratings, descriptions, prices, URLs, response generated by the LLM, and a summary of the review analysis. This information is stored in the Apify Dataset. The "best" product is determined by the LLM based on the input query. The Actor also stores Markdown and HTML files with the recommendation in the key-value store.

## Cost Considerations

The actor's cost is based on Apify platform usage (memory allocation) and OpenAI token consumption. The following events and prices apply:

```json
{
    "actor-start-gb": {
        "eventTitle": "Actor start per 1 GB",
        "eventDescription": "Flat fee for starting an Actor run for each 1 GB of memory.",
        "eventPriceUsd": 0.005
    },
    "openai-100-tokens-gpt-4o": {
        "eventTitle": "Price per 100 OpenAI tokens for gpt-4o",
        "eventDescription": "Flat fee for each 100 gpt-4o tokens used.",
        "eventPriceUsd": 0.001
    },
    "openai-100-tokens-gpt-4o-mini": {
        "eventTitle": "Price per 100 OpenAI tokens for gpt-4o-mini",
        "eventDescription": "Flat fee for each 100 gpt-4o-mini tokens used.",
        "eventPriceUsd": 0.00006
    },
    "openai-100-tokens-gpt-o1": {
        "eventTitle": "Price per 100 OpenAI tokens for o1",
        "eventDescription": "Flat fee for each 100 o1tokens used.",
        "eventPriceUsd": 0.006
    },
    "openai-100-tokens-gpt-o3-mini": {
        "eventTitle": "Price per 100 OpenAI tokens for o3-mini",
        "eventDescription": "Flat fee for each 100 o3-mini tokens used.",
        "eventPriceUsd": 0.00044
    }
}
```
