from fastapi import APIRouter, HTTPException
from app.models.summarize import SummarizeRequest, SummarizeResponse
from app.services.summarizer import summarize_text

router = APIRouter( # Create a router for summarization endpoints
    prefix="/summarize", # Prefix for all routes in this router
    tags=["summarize"]
)

@router.post("/", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="No text provided to summarize.")

    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)