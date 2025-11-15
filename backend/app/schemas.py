from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
class AssetBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    kind: str = 'video'
class AssetCreate(AssetBase):
    pass
class AssetRead(AssetBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes=True