from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI(
    title="Niblet CAD API",
    version="2.0.0"
)

class DesignRequest(BaseModel):
    design: dict[str, Any]

@app.get("/")
def root():
    return {
        "success": True,
        "message": "Niblet CAD API is running."
    }

@app.post("/generate")
def generate(request: DesignRequest):

    design = request.design

    # Later this entire dictionary goes into CadQuery

    return {
        "success": True,
        "message": "Design specification received.",
        "design": design
    }
