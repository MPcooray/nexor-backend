from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.organization import router as organization_router

app = FastAPI(title="Nexor Backend API")

app.include_router(auth_router, prefix="/api/v1")
app.include_router(organization_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Nexor Backend API is running"}