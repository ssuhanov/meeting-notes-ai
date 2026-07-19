from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "name": "Meeting Notes AI",
        "version": "1.0",
        "status": "running"
    }
