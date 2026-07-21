from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import cadquery as cq
import tempfile
import os

app = FastAPI(
    title="Niblet CAD API",
    version="3.0.0"
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

    # Temporary proof that CadQuery is working.
    # We'll replace this with a real cat generator next.

    model = (
        cq.Workplane("XY")
        .rect(13, 13)
        .extrude(1.0)
    )

    filename = f"{request.subject}_{request.product}.stl"
    filepath = os.path.join(tempfile.gettempdir(), filename)

    cq.exporters.export(model, filepath)

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="model/stl"
    )
