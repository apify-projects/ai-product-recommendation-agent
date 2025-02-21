"""This module defines Pydantic models for this project.

These models are used mainly for the structured tool and LLM outputs.
Resources:
- https://docs.pydantic.dev/latest/concepts/models/
"""

from __future__ import annotations

from pydantic import BaseModel


class AmazonProductPrice(BaseModel):
    """Amazon Product Price Pydantic model.

    value: The price value.
    currency: The currency of the price.
    """

    value: float
    currency: str


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
    features: list[str] | None = None


class AmazonReview(BaseModel):
    """Amazon Review Pydantic model.

    Returned as a structured output by the `tool_scrape_amazon_reviews` tool.

    ratingScore: The rating score of the review.
    reviewTitle: The title of the review.
    reviewDescription: The description of the review.
    """

    ratingScore: float
    reviewTitle: str
    reviewDescription: str


class RecommendedProduct(AmazonProduct, BaseModel):
    """Recommended Product Pydantic model.

    Returned as a structured output by the ReAct agent.

    reviewSummary: Longer summary of the reviews for this product.
    """

    reviewSummary: str | None = None


class AgentStructuredOutput(BaseModel):
    """Structured output for the ReAct agent.

    Returned as a structured output by the ReAct agent.

    recommended_products: List of recommended Amazon products.
    """

    recommended_products: list[RecommendedProduct]
