from pydantic import BaseModel
from uuid import UUID


class DepartmentCreate(BaseModel):
    name: str
    description: str | None = None
    criticality_level: str = "medium"


class DepartmentResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    criticality_level: str

    class Config:
        from_attributes = True


class LocationCreate(BaseModel):
    name: str
    country: str | None = None
    type: str | None = None


class LocationResponse(BaseModel):
    id: UUID
    name: str
    country: str | None
    type: str | None

    class Config:
        from_attributes = True


class RoleCreate(BaseModel):
    department_id: UUID
    role_name: str
    criticality_level: str = "medium"


class RoleResponse(BaseModel):
    id: UUID
    department_id: UUID
    role_name: str
    criticality_level: str

    class Config:
        from_attributes = True