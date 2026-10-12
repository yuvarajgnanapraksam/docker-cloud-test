
from fastapi import FastAPI

app = FastAPI(
    title="Employee Management API",
    description="API for managing employee information",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
