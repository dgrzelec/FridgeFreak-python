from datetime import date
from httpx import AsyncClient
import pytest
from typing import List
from fridgefreak_api.models import Product
from fridgefreak_api.tests.test_post_products import created_products

product_id = 2
updated_product = {"name": "tomato", 
                    "quantity": 2, 
                    "category": "VEGETABLE", 
                    "storage_space": "FRIDGE",
                    "expire_by": str(date(2024,1,1))}


async def update_product_id(id: int, async_client: AsyncClient) -> dict:
    response =  await async_client.put(f"/api/storage/{id}", json=updated_product)
    return response.json()

@pytest.fixture
async def updated_product_id(async_client: AsyncClient):
    return await update_product_id(product_id, async_client)

@pytest.mark.anyio
async def test_put_product(async_client: AsyncClient, created_products: dict):
    body = updated_product
    response  = await async_client.put(f"/api/storage/{product_id}", json=body)
    assert response.status_code == 200

@pytest.mark.anyio
async def test_updated_product(async_client: AsyncClient, created_products: dict, updated_product_id: dict):
    prod_id = updated_product_id["id"]

    response  = await async_client.get(f"/api/storage/{prod_id}")
    assert response.status_code == 200
    assert response.json()["quantity"] == 2