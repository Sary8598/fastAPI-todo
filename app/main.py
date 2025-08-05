from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="TODO API",
    description="API to manage todos with FastAPI and authentication",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status: Annotated[str, "API actual status"]
    message: Annotated[str,"Descriptive message"]

@app.get("/health", response_model=HealthResponse, tags=["System"])
def check_health() -> HealthResponse:
    return HealthResponse(status="ok", message="API is working correctly")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        workers=1
    )