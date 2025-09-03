from fastapi import FastAPI
from app.routes import summarize

app = FastAPI(title="Summarizer API")

# Register routes
app.include_router(summarize.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Summarizer API"}

