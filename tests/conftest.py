import asyncio
import pytest
from store_api.db.mongo import db_client
from store_api.schemas.products import ProductIn
from uuid import UUID
from tests.factories import product_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True, scope="function")
async def clear_collections(mongo_client):
    yield
    db = mongo_client.get_database()
    collections = await db.list_collection_names()
    for collection in collections:
        if collection.startswith("system"):
            continue

        await db[collection].delete_many({})


def pytest_collection_modifyitems(items):
    for item in items:
        if "schemas" in str(item.fspath):
            item.fixturenames = [
                f for f in item.fixturenames if f != "clear_collections"
            ]


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("aa61b318-7dd4-4d76-acc6-5508f1152b3d")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)
