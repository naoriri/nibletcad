from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Niblet CAD API",
    version="1.0.0"
)


class GenerateRequest(BaseModel):
    product: str
    subject: str
    style: str | None = None


@app.get("/")
def root():
    return {
        "success": True,
        "message": "Niblet CAD API is running."
    }


@app.post("/generate")
def generate(request: GenerateRequest):
    return {
        "success": True,
        "status": "received",
        "request": request.model_dump()
    }
