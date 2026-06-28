import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func

from app.db.database import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    domain = Column(String(255), unique=True, nullable=False)
    country = Column(String(100))
    status = Column(String(50), default="active")
    subscription_plan = Column(String(100))
    enabled_modules = Column(JSONB, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())