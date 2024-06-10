from httpx import AsyncClient
import pytest
from typing import List
from fridgefreak_api.models import Product

sample_products =  [
                    {
                    "name": "eggs",
                    "quantity": 10,
                    "category": "OTHER",
                    "storage_space": "FRIDGE",
                    "expire_by": "2023-07-31"
                    },
                    {
                    "name": "tomato",
                    "quantity": 1,
                    "category": "VEGETABLE",
                    "storage_space": "FRIDGE",
                    "expire_by": "2023-07-22"
                    },
                    {
                    "name": "Milk",
                    "quantity": 2,
                    "category": "DIARY",
                    "storage_space": "FRIDGE",
                    "expire_by": "2023-07-25"
                    },
                    {
                    "name": "Ham",
                    "quantity": 3,
                    "category": "MEAT",
                    "storage_space": "FRIDGE",
                    "expire_by": "2023-07-25"
                    },
                    {
                    "name": "Apple",
                    "quantity": 5,
                    "category": "FRUIT",
                    "storage_space": "SHELF",
                    "expire_by": "2023-07-25"
                    },
                    {
                    "name": "Pepper",
                    "quantity": 1,
                    "category": "SPICE",
                    "storage_space": "SHELF",
                    "expire_by": "2023-07-25"
                    }
                ]

async def create_products(body: List[Product], async_client: AsyncClient) -> dict:
    response  = await async_client.post("/api/storage", json=body)
    return response.json()

@pytest.fixture
async def created_products(async_client: AsyncClient):
    return await create_products(sample_products, async_client)


@pytest.mark.anyio
async def test_create_products(async_client: AsyncClient):
    body = sample_products

    print(body)

    response  = await async_client.post(
            "/api/storage", 
            json=body
    )
    
    assert response.status_code == 201
    assert {"message": f"Added {len(sample_products)} products"}.items() <= response.json().items()
