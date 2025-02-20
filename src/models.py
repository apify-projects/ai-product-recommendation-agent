"""This module defines Pydantic models for this project.

These models are used mainly for the structured tool and LLM outputs.
Resources:
- https://docs.pydantic.dev/latest/concepts/models/
"""

from __future__ import annotations

from pydantic import BaseModel

class AmazonProductPrice(BaseModel):
    value: float
    currency: str


class InstagramPost(BaseModel):
    """Instagram Post Pydantic model.

    Returned as a structured output by the `tool_scrape_instagram_profile_posts` tool.

    url: The URL of the post.
    likes: The number of likes on the post.
    comments: The number of comments on the post.
    timestamp: The timestamp when the post was published.
    caption: The post caption.
    alt: The post alt text.
    """

    url: str
    likes: int
    comments: int
    timestamp: str
    caption: str | None = None
    alt: str | None = None

class AmazonProduct(BaseModel):
    """Amazon Product Pydantic model.

    Returned as a structured output by the `tool_scrape_amazon_products` tool.

    title: The title of the product.
    brand: The brand of the product.
    stars: The rating of the product.
    description: The description of the product.
    price: The price of the product.
    url: The URL of the product.
    """
    title: str
    brand: str | None = None
    stars: float | None = None
    description: str | None = None
    price: AmazonProductPrice | None = None
    url: str | None = None



class AgentStructuredOutput(BaseModel):
    """Structured output for the ReAct agent.

    Returned as a structured output by the ReAct agent.

    total_likes: The total number of likes on the most popular posts.
    total_comments: The total number of comments on the most popular posts.
    most_popular_posts: A list of the most popular posts.
    """

    total_likes: int
    total_comments: int
    most_popular_posts: list[InstagramPost]
