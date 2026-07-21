from fastapi import FastAPI
from pydantic import BaseModel
import cadquery as cq
import tempfile
import os

app = FastAPI(
    title="Niblet CAD API",
    version="1.0.0"
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

    model = (
        cq.Workplane("XY")
        .box(18, 18, 5)
    )

    temp_dir = tempfile.gettempdir()
    filename = f"{request.subject}_{request.product}.stl"
    filepath = os.path.join(temp_dir, filename)

    cq.exporters.export(model, filepath)

    return {
        "success": True,
        "message": "STL generated successfully.",
        "product": request.product,
        "subject": request.subject,
        "style": request.style,
        "stl_created": True,
        "stl_path": filepath
    }
