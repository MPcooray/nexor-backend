from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.organization import (
    DepartmentCreate,
    DepartmentResponse,
    LocationCreate,
    LocationResponse,
    RoleCreate,
    RoleResponse,
)
from app.services.organization_service import (
    create_department,
    create_location,
    create_role,
    get_departments,
    get_locations,
    get_roles,
)

router = APIRouter(
    prefix="/organization",
    tags=["Organization Setup"]
)


@router.post("/departments", response_model=DepartmentResponse)
def create_department_endpoint(
    payload: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_department(db, current_user.tenant_id, payload)


@router.get("/departments", response_model=List[DepartmentResponse])
def get_departments_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_departments(db, current_user.tenant_id)


@router.post("/locations", response_model=LocationResponse)
def create_location_endpoint(
    payload: LocationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_location(db, current_user.tenant_id, payload)


@router.get("/locations", response_model=List[LocationResponse])
def get_locations_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_locations(db, current_user.tenant_id)


@router.post("/roles", response_model=RoleResponse)
def create_role_endpoint(
    payload: RoleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_role(db, current_user.tenant_id, payload)


@router.get("/roles", response_model=List[RoleResponse])
def get_roles_endpoint(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_roles(db, current_user.tenant_id)