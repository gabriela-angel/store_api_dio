from store_api.schemas.products import ProductOut
from store_api.usecases.products import usecase


async def test_usecases_create_return_success(product_in):
    result = await usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == product_in.name
    # print(result.id)


async def test_usecases_get_return_success(product_id):
    result = await usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    # assert result.name == "Test Product"
