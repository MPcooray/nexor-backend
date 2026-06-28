from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.tenant import Tenant
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterCompanyRequest


def register_company(db: Session, payload: RegisterCompanyRequest):
    existing_tenant = db.query(Tenant).filter(Tenant.domain == payload.company_domain).first()

    if existing_tenant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company domain already registered"
        )

    existing_user = db.query(User).filter(User.email == payload.admin_email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin email already registered"
        )

    tenant = Tenant(
        name=payload.company_name,
        domain=payload.company_domain,
        country=payload.country,
        status="active"
    )

    db.add(tenant)
    db.flush()

    admin_user = User(
        tenant_id=tenant.id,
        email=payload.admin_email,
        name=payload.admin_name,
        role="organization_admin",
        status="active",
        password_hash=hash_password(payload.admin_password)
    )

    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)

    access_token = create_access_token(
        data={
            "sub": str(admin_user.id),
            "tenant_id": str(admin_user.tenant_id),
            "role": admin_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def login(db: Session, payload: LoginRequest):
    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "tenant_id": str(user.tenant_id),
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }