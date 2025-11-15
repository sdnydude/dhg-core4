import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from .db import Base
class Asset(Base):
    __tablename__='assets'
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    title=Column(String,nullable=False)
    description=Column(String,nullable=True)
    kind=Column(String,nullable=False,default='video')
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)