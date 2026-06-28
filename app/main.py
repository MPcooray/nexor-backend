from fastapi import FastAPI

app = FastAPI(title="Nexor Backend API")


@app.get("/")
def root():
    return {"message": "Nexor Backend API is running"}