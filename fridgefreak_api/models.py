# generated by fastapi-codegen:
#   filename:  ./FridgeFreak API/fridgefreak-api_OAS3.yaml
#   timestamp: 2024-06-06T14:21:29+00:00

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, RootModel


class Category(Enum):
    MEAT = 'MEAT'
    DIARY = 'DIARY'
    VEGETABLE = 'VEGETABLE'
    FRUIT = 'FRUIT'
    SPICE = 'SPICE'
    OTHER = 'OTHER'


class StorageSpace(Enum):
    FRIDGE = 'FRIDGE'
    SHELF = 'SHELF'
    OTHER = 'OTHER'


class Product(BaseModel):
    name: str = None
    quantity: int = None
    category: Category = None
    storage_space: StorageSpace = None
    expire_by: date = None


class StorageGetResponse(BaseModel):
    result_count: int
    products: List[Product]


class StoragePostRequest(RootModel):
    root: List[Product]


class StorageDeleteRequest(BaseModel):
    name: Optional[str] = None
    storage_space: Optional[str] = None
    category: Optional[str] = None
    expire_by: Optional[date] = None


class ProductNotFoundResponse(BaseModel):
    message: str