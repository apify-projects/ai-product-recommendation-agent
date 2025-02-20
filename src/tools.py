"""This module defines the tools used by the agent.

Feel free to modify or add new tools to suit your specific needs.

To learn how to create a new tool, see:
- https://python.langchain.com/docs/concepts/tools/
- https://python.langchain.com/docs/how_to/#tools
"""

from __future__ import annotations

from apify import Actor
from langchain_core.tools import tool
from pydantic import BaseModel

from src.models import AmazonProduct, AmazonProductPrice, AmazonReview

class CategoryOrProductUrl(BaseModel):
    """
    Pydantic model for a category or
    product URL to scrape.

    url: The URL to scrape. Example: https://www.amazon.com/s?k=laptop&low-price=400&high-price=600
    method: The HTTP method to use. Example: GET
    """
    url: str
    method: str

class ProductUrl(BaseModel):
    """
    Pydantic model for a product URL to scrape.

    url: The URL to scrape. Example: https://www.amazon.com/dp/B08P3K8H5P
    method: The HTTP method to use. Example: GET
    """
    url: str
    method: str


@tool
async def tool_scrape_amazon_products(category_or_product_urls: list[CategoryOrProductUrl], max_items_per_start_url: int = 50) -> list[AmazonProduct]:
    """Tool to scrape Amazon products.

    Args:
        category_or_product_urls (list[CategoryOrProductUrl]): List of category or product URLs to scrape. At least one URL must be provided.
        max_items_per_start_url (int, optional): Maximum number of items per start url to scrape. Defaults to 50.

    Returns:
        list[AmazonProduct]: List of Amazon products scraped.

    Raises:
        RuntimeError: If the Actor fails to start.
    """
    if len(category_or_product_urls) < 1:
        raise ValueError('At least one category or product URL must be provided.')

    run_input = {
        "categoryOrProductUrls": [item.model_dump() for item in category_or_product_urls],
        "maxItemsPerStartUrl": max_items_per_start_url,
        "maxOffers": 1,
    }
    if not (run := await Actor.apify_client.actor('junglee/Amazon-crawler').call(run_input=run_input)):
        msg = 'Failed to start the Actor junglee/Amazon-crawler'
        raise RuntimeError(msg)

    dataset_id = run['defaultDatasetId']
    dataset_items: list[dict] = (await Actor.apify_client.dataset(dataset_id).list_items()).items
    products: list[AmazonProduct] = []
    for item in dataset_items:
        title: str | None = item.get('title')
        brand: str | None = item.get('brand')
        stars: int | None = item.get('stars')
        description: str | None = item.get('description')
        price: dict | None = item.get('price')
        url: str | None = item.get('url')

        products.append(
            AmazonProduct(
                title=title,
                brand=brand,
                stars=stars,
                description=description,
                price=AmazonProductPrice(**price) if price else None,
                url=url,
            )
        )

    return products

@tool
async def tool_scrape_amazon_reviews(product_urls: list[ProductUrl], max_reviews: int = 50) -> list[AmazonReview]:
    """
    Tool to scrape Amazon reviews.

    Args:
        product_urls (list[ProductUrl]): List of product URLs to scrape.
        max_reviews (int, optional): Maximum number of reviews to scrape per product. Defaults to 50.

    Returns:
        list[AmazonReview]: List of Amazon reviews scraped from the product URLs.

    """
    run_input = {
        "productUrls": [item.model_dump() for item in product_urls],
        "maxReviews": max_reviews,
    }
    if not (run := await Actor.apify_client.actor('junglee/amazon-reviews-scraper').call(run_input=run_input)):
        msg = 'Failed to start the Actor junglee/amazon-reviews-scraper'
        raise RuntimeError(msg)

    dataset_id = run['defaultDatasetId']
    dataset_items: list[dict] = (await Actor.apify_client.dataset(dataset_id).list_items()).items
    reviews: list[AmazonProduct] = []
    for item in dataset_items:
        ratingScore: float = item.get('ratingScore')
        reviewTitle: str = item.get('reviewTitle')
        reviewDescription: str = item.get('reviewDescription')

        reviews.append(
            AmazonReview(
                ratingScore=ratingScore,
                reviewTitle=reviewTitle,
                reviewDescription=reviewDescription,
            )
        )

    return reviews


@tool
def tool_get_prompt_for_amazon_product_list_plain_url(query: str) -> str:
    """Tool to get the right prompt for the Amazon product list URL.

    Args:
        query (str): User query.
    Returns:
        str: Prompt for the Amazon product list URL.
    """
    return f"Generate an Amazon search URL for {query}, including relevant filters like price if mentioned."