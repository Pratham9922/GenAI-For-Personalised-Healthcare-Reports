from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_handler import generate_report_from_symptoms

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomRequest(BaseModel):
    symptoms: str

@app.post("/generate-report")
def generate_report(request: SymptomRequest):
    report = generate_report_from_symptoms(request.symptoms)
    return {"report": report}