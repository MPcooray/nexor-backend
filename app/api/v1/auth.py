from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.auth import LoginRequest, RegisterCompanyRequest, TokenResponse
from app.services.auth_service import login, register_company

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register-company", response_model=TokenResponse)
def register_company_endpoint(
    payload: RegisterCompanyRequest,
    db: Session = Depends(get_db)
):
    return register_company(db, payload)


@router.post("/login", response_model=TokenResponse)
def login_endpoint(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    return login(db, payload)