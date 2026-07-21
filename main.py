from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import cadquery as cq
import tempfile
import os

app = FastAPI(
    title="Niblet CAD API",
    version="4.0.0"
)

OUTPUT_DIR = os.path.join(tempfile.gettempdir(), "generated_models")
os.makedirs(OUTPUT_DIR, exist_ok=True)


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

    # Temporary placeholder.
    # Later GPT will generate the actual geometry.

    model = (
        cq.Workplane("XY")
        .rect(13, 13)
        .extrude(1.0)
    )

    filename = f"{request.subject}_{request.product}.stl"
    filepath = os.path.join(OUTPUT_DIR, filename)

    cq.exporters.export(model, filepath)

    return {
        "success": True,
        "filename": filename,
        "download_url": f"/files/{filename}"
    }


@app.get("/files/{filename}")
def download_file(filename: str):

    filepath = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(filepath):
        return {
            "success": False,
            "message": "File not found."
        }

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="model/stl"
    )
