from httpx import AsyncClient
import pytest
from typing import List
from fridgefreak_api.models import Product
from fridgefreak_api.tests.test_post_products import sample_products, created_products

@pytest.mark.anyio
async def test_product_filtering(async_client: AsyncClient, created_products: dict):
    
    # all products
    response = await async_client.get("/api/storage")
    assert response.status_code == 200
    assert {"result_count": len(sample_products)}.items() <= response.json().items()

    # Name filtering
    response = await async_client.get("/api/storage", params={"name": "Milk"})
    assert response.status_code == 200
    assert {"result_count": 1}.items() <= response.json().items()
    assert response.json()["products"][0]["name"] == "Milk"


@pytest.mark.anyio
async def test_product_get_id(async_client: AsyncClient, created_products: dict):

    response = await async_client.get("/api/storage/0")
    assert response.status_code == 200

    response = await async_client.get("/api/storage/7")
    assert response.status_code == 404