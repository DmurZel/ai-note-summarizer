from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.summarizer import summarize_text

router = APIRouter(
    prefix="/summarize",
    tags=["summarize"]
)

# Request body model
class SummarizeRequest(BaseModel):
    text: str

# Response model
class SummarizeResponse(BaseModel):
    summary: str

@router.post("/", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="No text provided to summarize.")

    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)