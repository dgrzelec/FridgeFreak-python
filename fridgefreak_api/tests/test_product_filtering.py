from httpx import AsyncClient
import pytest
from typing import List
from fridgefreak_api.models import Product
from fridgefreak_api.tests.test_post_products import sample_products, created_products

@pytest.mark.anyio
async def test_product_filtering_no_params(async_client: AsyncClient, created_products: dict):
    
    # all products
    response = await async_client.get("/api/storage")
    assert response.status_code == 200
    assert {"result_count": len(sample_products)}.items() <= response.json().items()

@pytest.mark.anyio
async def test_product_filtering_1_param(async_client: AsyncClient, created_products: dict):
    # Name filtering
    response = await async_client.get("/api/storage", params={"name": "Milk"})
    assert response.status_code == 200
    assert {"result_count": 1}.items() <= response.json().items()
    assert response.json()["products"][0]["name"] == "Milk"

@pytest.mark.anyio
async def test_product_filtering_all_params(async_client: AsyncClient, created_products: dict):
    # all fields
    response = await async_client.get("/api/storage", params={"name": "eggs", 
                                                              "category": "OTHER", 
                                                              "quantity": 10, 
                                                              "storage_space": "FRIDGE"})
    assert response.status_code == 200
    assert {"result_count": 1}.items() <= response.json().items()
    assert response.json()["products"][0]["name"] == "eggs"

@pytest.mark.anyio
async def test_product_filtering_not_found(async_client: AsyncClient, created_products: dict):
    response = await async_client.get("/api/storage", params={"name": "tomato", 
                                                              "category": "FRUIT", 
                                                              "quantity": 1, 
                                                              "storage_space": "FRIDGE"})
    assert response.status_code == 404




@pytest.mark.anyio
async def test_product_get_id(async_client: AsyncClient, created_products: dict):

    response = await async_client.get("/api/storage/1")
    assert response.status_code == 200

    response = await async_client.get("/api/storage/7")
    assert response.status_code == 404