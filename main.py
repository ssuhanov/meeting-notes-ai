from fastapi import FastAPI

from models import MeetingRequest
from services import analyze_notes

app = FastAPI()

@app.get("/")
def hello():
    return {
        "name": "Meeting Notes AI",
        "version": "1.0",
        "status": "running"
    }

@app.post("/analyze")
def analyze(request: MeetingRequest):
    result = analyze_notes(request.notes)
    return result
