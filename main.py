from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "success": True,
        "message": "Hello from Niblet CAD API!"
    }
