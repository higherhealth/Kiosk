from pydantic import BaseModel
from typing import List, Optional


class Product(BaseModel):
    product_id: str
    name: str
    category: str
    price: float
    available: bool
    tags: List[str] = []
    margin_score: float = 0.5


class RecommendationRequest(BaseModel):
    intent: str
    budget: float


class RecommendationResponse(BaseModel):
    primary: Product
    upsells: List[Product]
    explanation: str
