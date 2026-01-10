#!/bin/bash

# Kill anything running on port 8000
lsof -t -i:8000 | xargs -r kill -9

# Activate virtual environment
source venv/bin/activate

# Start the FastAPI app
echo "Starting FastAPI server..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload