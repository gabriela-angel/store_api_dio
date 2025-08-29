from datetime import datetime
from pydantic import BaseModel, Field, UUID4, ConfigDict
from uuid import uuid4


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid4, description="Unique identifier")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=datetime.now, description="Last update timestamp"
    )

    model_config = ConfigDict(
        from_attributes=True,  # substitui orm_mode=True
        validate_by_name=True,  # substitui allow_population_by_field_name=True
        json_serializers={datetime: lambda v: v.isoformat()},  # substitui json_encoders
    )
