from store_api.schemas.products import ProductIn
import pytest
from pydantic import ValidationError
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)
    # either that, or product = ProductIn(**data)

    assert product.name == "Test Product"


# We found the error info by adding a breakpoint() after
# the with statement, searching for "err" in the variables list,
# dir(err) and then err.value.errors()
def test_schemas_return_raise():
    data = {
        "name": "Test Product",
        "price": 12.000,
        "quantity": 10,
        "description": "A test product",
    }

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {
            "name": "Test Product",
            "price": 12.0,
            "quantity": 10,
            "description": "A test product",
        },
        "url": "https://errors.pydantic.dev/2.11/v/missing",
    }
