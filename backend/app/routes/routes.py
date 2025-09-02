from fastapi import APIRouter
from .summarizer import summarize_text

router = APIRouter()

@router.get("/")
def root():
    return {"message": "AI Note Summarizer backend is running."}

@router.post("/summarize")
def summarize_endpoint(text: str):
    summary = summarize_text(text)
    return {"summary": summary}