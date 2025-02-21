# Development

## Getting started
First, clone this repository.

```bash
apify run # Run locally
apify push # Deploy to Apify
```

## Input

```json
{
    "query": "suggest me best laptop that is not too expensive but has really good stats and price under $600"
}
```

## Output

The actor outputs data to the Apify Dataset. Each item in the dataset contains the following fields:

| Field           | Type   | Description                                                             |
| --------------- | ------ | ----------------------------------------------------------------------- |
| `title`         | String | The title of the product.                                               |
| `brand`         | String | The brand of the product.                                               |
| `stars`         | Number | The average star rating of the product.                                 |
| `description`   | String | The product description.                                                |
| `price`         | Object | The product price, containing `value` (Number) and `currency` (String). |
| `url`           | String | The URL of the product page.                                            |
| `response`      | String | The LLM generated message for the query.                                |
| `reviewSummary` | String | A summary of the review analysis.                                       |

## Example Output

```json
[
    {
        "title": "Lenovo IdeaPad 1 Student Laptop",
        "brand": "Lenovo",
        "stars": 4.4,
        "description": "15.6\" FHD Display, Intel Dual Core Processor, 16GB DDR4 RAM, 256GB PCIe SSD, WiFi 6, Bluetooth 5.2, Type-C, Cloud Grey, Windows 11 Pro",
        "price": {
            "value": 299,
            "currency": "$"
        },
        "url": "https://www.amazon.com/dp/B0DSPVNWWK",
        "reviewSummary": "A great budget laptop for college-level work. Fast business machine with good overall performance. Lightweight and easy to use.",
        "response": "Here are some of the best laptops under $600 that come with solid specifications and positive reviews:\n\n### 1. **Lenovo IdeaPad 1**\n- **Price:** $299.00\n- **Specs:** 15.6\" FHD Display, Intel Dual Core Processor, 16GB RAM, 256GB PCIe SSD, WiFi 6, Bluetooth 5.2, Windows 11 Pro\n- **Rating:** 4.4/5\n- **Link:** [View on Amazon](https://www.amazon.com/dp/B0DSPVNWWK)\n  \n**Pros:**\n  - Affordable price\n  - Ample RAM and storage for everyday tasks\n  - Good battery life and performance for college-level work\n\n**Cons:**\n  - Lacks a backlit keyboard\n  - Average screen viewing angles\n\n**Review Summary:** Users praise the Lenovo IdeaPad for its performance and value for money, perfect for students and light gaming. \n\n---\n\n### 2. **Acer Aspire 3 A315-24P**\n- **Price:** $299.99\n- **Specs:** 15.6\" Full HD IPS Display, AMD Ryzen 3 7320U Quad-Core Processor, AMD Radeon Graphics, 8GB RAM, 128GB NVMe SSD, Wi-Fi 6, Windows 11 Home\n- **Rating:** 4.2/5\n- **Link:** [View on Amazon](https://www.amazon.com/dp/B0BS4BP8FB)\n\n**Pros:**\n  - Good display quality (IPS)\n  - Good performance for everyday tasks and casual gaming\n  - Sleek design\n\n**Cons:**\n  - Limited storage space\n  - Average build quality\n\n**Review Summary:** Many appreciate the Acer Aspire for its graphics and speed, making it suitable for schoolwork and regular use.\n\n---\n\n### 3. **HP Pavilion**\n- **Price:** $599.00\n- **Specs:** 15.6\" FHD, Intel Core 8-Core CPU, 32GB RAM, 1TB Storage\n- **Rating:** 4.3/5\n- **Link:** [View on Amazon](https://www.amazon.com/dp/B0DN7YC7R8)\n\n**Pros:**\n  - High RAM and storage capacity\n  - Good performance for multitasking\n  - Fingerprint reader for added security\n\n**Cons:**\n  - Heavier than competitors\n  - Battery life can be less than expected\n\n**Review Summary:** This model is highly recommended for users who need a powerful laptop for multitasking and storage. \n\n---\n\n### 4. **HP Victus Gaming Laptop**\n- **Price:** $575.00\n- **Specs:** 15.6” FHD IPS 144Hz, Intel 8-core i5-12450H, 16GB RAM, 512GB SSD, GeForce RTX 3050\n- **Rating:** 4.6/5\n- **Link:** [View on Amazon](https://www.amazon.com/dp/B0DGSMZ54J)\n\n**Pros:**\n  - Great for gaming and demanding applications\n  - Excellent display with 144Hz refresh rate\n  - Good build quality\n\n**Cons:**\n  - Heavy battery drain during gaming sessions\n  Limited battery life under heavy use\n\n**Review Summary:** The HP Victus is praised for its gaming capabilities and performance but is noted for shorter battery life while gaming.\n\n---\n\n### 5. **Lenovo V15**\n- **Price:** $499.00\n- **Specs:** 15.6\" FHD Display, AMD Ryzen 5 5500U, 16GB RAM, 512GB SSD\n- **Rating:** 4.3/5\n- **Link:** [View on Amazon](https://www.amazon.com/dp/B0CK9JSM3G)\n\n**Pros:**\n  - Solid performance for its price\n  - Good battery life\n  - Stylish design\n\n**Cons:**\n  - Basic design may not appeal to everyone\n  - The display could be better in terms of brightness\n\n**Review Summary:** Users find this laptop to be a balanced option for general use and work, providing a decent performance at a reasonable price.\n\n---\n\nOverall, the **Lenovo IdeaPad 1** and **Acer Aspire 3** stand out for their affordability while maintaining good specs for everyday tasks. For a more gaming-focused experience, the **HP Victus** provides great value within your budget."
    }
    //... other products
]
```

## Documentation reference

-   [LangGraph documentation](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
-   [LangChain documentation](https://python.langchain.com/docs/introduction/)
-   [Apify Python SDK documentation](https://docs.apify.com/sdk/python/)
-   [`junglee/Amazon-crawler` actor](https://apify.com/junglee/Amazon-crawler)
-   [`junglee/amazon-reviews-scraper` actor](https://apify.com/junglee/amazon-reviews-scraper)
-   [Apify Platform documentation](https://docs.apify.com/platform)
-   [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)

## Limitations

-   Relies on the stability and availability of the `junglee/Amazon-crawler` and `junglee/amazon-reviews-scraper` actors.
-   The quality of the review analysis depends on the complexity of the agent and the available review data.
-   OpenAI API key is required and should be provided as an environment variable (`OPENAI_API_KEY`).
-   Amazon's website structure may change, potentially breaking the scrapers.
