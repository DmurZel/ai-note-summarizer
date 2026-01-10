from fastapi import FastAPI # Import FastAPI
from app.routes import summarize # Import summarize router
from dotenv import load_dotenv
load_dotenv()
#Backend Server
# Defines API routes that clients(curl, frontend, Swagger UI) can call
#Runs with Uvicorn, which is the ASGI web server

#This is defined as a POST endpoint
#It expects JSON input with field ike
# {"text": "some text to summarize"}

# Initialize FastAPI app
app = FastAPI(title="Summarizer API")# Summarizer API

# Register routes
app.include_router(summarize.router)# Include the summarize router

# Root endpoint
@app.get("/")# Welcome message
def root():
    return {"message": "Welcome to the Summarizer API"}# Run with: uvicorn app.main:app --reload

