from fastapi import FastAPI

from app.api.v1.auth import router as auth_router

app = FastAPI(title="Nexor Backend API")

app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Nexor Backend API is running"}