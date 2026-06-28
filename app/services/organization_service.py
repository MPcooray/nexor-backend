from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.department import Department
from app.models.location import Location
from app.models.role_definition import RoleDefinition
from app.schemas.organization import DepartmentCreate, LocationCreate, RoleCreate


def create_department(db: Session, tenant_id, payload: DepartmentCreate):
    department = Department(
        tenant_id=tenant_id,
        name=payload.name,
        description=payload.description,
        criticality_level=payload.criticality_level,
    )
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def get_departments(db: Session, tenant_id):
    return db.query(Department).filter(Department.tenant_id == tenant_id).all()


def create_location(db: Session, tenant_id, payload: LocationCreate):
    location = Location(
        tenant_id=tenant_id,
        name=payload.name,
        country=payload.country,
        type=payload.type,
    )
    db.add(location)
    db.commit()
    db.refresh(location)
    return location


def get_locations(db: Session, tenant_id):
    return db.query(Location).filter(Location.tenant_id == tenant_id).all()


def create_role(db: Session, tenant_id, payload: RoleCreate):
    department = db.query(Department).filter(
        Department.id == payload.department_id,
        Department.tenant_id == tenant_id,
    ).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    role = RoleDefinition(
        tenant_id=tenant_id,
        department_id=payload.department_id,
        role_name=payload.role_name,
        criticality_level=payload.criticality_level,
    )
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_roles(db: Session, tenant_id):
    return db.query(RoleDefinition).filter(RoleDefinition.tenant_id == tenant_id).all()
