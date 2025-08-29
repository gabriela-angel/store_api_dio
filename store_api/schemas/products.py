from pydantic import field_validator, Field
from store_api.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    # The three dots (...) indicate that the field is required
    name: str = Field(..., description="Product name", min_length=1, max_length=100)
    price: float = Field(..., description="Product price", gt=0)
    quantity: int = Field(..., description="Available quantity", ge=0)
    status: bool = Field(..., description="Product availability status")
    description: str | None = Field(
        default=None, description="Product description", max_length=200
    )

    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Price must be a positive number")
        return v

    @field_validator("quantity")
    def quantity_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("Quantity must be a non-negative integer")
        return v


class ProductOut(ProductIn):
    pass
