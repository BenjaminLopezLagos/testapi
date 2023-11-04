import uuid
from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime


class Food(BaseModel):
    food_id: str
    group: str


class History(BaseModel):
    region: str
    price: int
    date: datetime


class FoodWithHistory(BaseModel):
    food_id: str
    group: str
    prices: List[History]
