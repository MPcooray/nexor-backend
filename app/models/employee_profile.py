import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func

from app.db.database import Base


class EmployeeProfile(Base):
    __tablename__ = "employee_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tenants.id", ondelete="CASCADE"),
        nullable=False
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=True
    )

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("role_definitions.id"),
        nullable=True
    )

    location_id = Column(
        UUID(as_uuid=True),
        ForeignKey("locations.id"),
        nullable=True
    )

    work_type = Column(String(50))
    seniority = Column(String(50))

    questionnaire_answers = Column(JSONB, default={})

    created_at = Column(DateTime(timezone=True), server_default=func.now())