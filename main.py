from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Niblet CAD API",
    version="2.0.0"
)

class GenerateRequest(BaseModel):
    product: str
    subject: str
    style: str = "default"

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
        "message": "Request received.",
        "product": request.product,
        "subject": request.subject,
        "style": request.style
    }
