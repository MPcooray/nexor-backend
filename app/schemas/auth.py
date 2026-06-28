from pydantic import BaseModel, EmailStr


class RegisterCompanyRequest(BaseModel):
    company_name: str
    company_domain: str
    country: str | None = None
    admin_name: str
    admin_email: EmailStr
    admin_password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthUserResponse(BaseModel):
    id: str
    tenant_id: str | None
    email: EmailStr
    name: str | None
    role: str
    status: str