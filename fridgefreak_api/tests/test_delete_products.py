from httpx import AsyncClient
import pytest
from typing import List
from fridgefreak_api.models import Product
from fridgefreak_api.tests.test_post_products import created_products

product_id = 1

async def delete_product_id(id: int, async_client: AsyncClient) -> dict:
    response  = await async_client.delete(f"/api/storage/{id}")
    return response.json()

@pytest.fixture
async def deleted_product_id(async_client: AsyncClient):
    return await delete_product_id(product_id, async_client)

@pytest.mark.anyio
async def test_delete_product_match(async_client: AsyncClient, created_products: dict):
    
    body = {"name": "eggs", "storage_space": "FRIDGE"}
    response  = await async_client.request("delete", f"/api/storage", params={"in-database": False}, json=body)
    assert response.status_code == 200
    # check if quantity of this item is zero
    response  = await async_client.get(f"/api/storage", params=body)
    assert response.status_code == 200
    assert response.json()["products"][0]["quantity"] == 0

@pytest.mark.anyio
async def test_delete_product_match_in_database(async_client: AsyncClient, created_products: dict):
    
    body = {"name": "eggs", "storage_space": "FRIDGE"}
    response  = await async_client.request("delete", f"/api/storage", params={"in-database": True}, json=body)
    assert response.status_code == 200
    prod_id = response.json()["id"]
    # check if the item is deleted
    response  = await async_client.get(f"/api/storage/{prod_id}")
    assert response.status_code == 404

@pytest.mark.anyio
async def test_delete_product_not_found(async_client: AsyncClient, created_products: dict):
    
    body = {"name": "better_eggs", "storage_space": "FRIDGE"}
    response  = await async_client.request("delete", f"/api/storage", params={"in-database": False}, json=body)
    assert response.status_code == 404
    
@pytest.mark.anyio
async def test_delete_product_multiple_found(async_client: AsyncClient, created_products: dict):
    
    body = {"storage_space": "FRIDGE"}
    response  = await async_client.request("delete", f"/api/storage", params={"in-database": False}, json=body)
    assert response.status_code == 500    

@pytest.mark.anyio
async def test_product_delete_by_id(async_client: AsyncClient, created_products: dict):
    
    response  = await async_client.delete(f"/api/storage/{product_id}")
    assert response.status_code == 200
    assert {"message": f"Product with id {product_id} deleted"}.items() <= response.json().items()

    response  = await async_client.delete(f"/api/storage/7")
    assert response.status_code == 404
