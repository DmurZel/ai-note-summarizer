from fastapi import FastAPI
from app.routes.notes import router as notes_router
from app.routes.summarize import router as summarize_router

app.include_router(notes_router)
app.include_router(summarize_router)


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Note Summarizer backend is running."}