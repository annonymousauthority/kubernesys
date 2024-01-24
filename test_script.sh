#!/bin/bash

# Run FastAPI server
uvicorn main:app --reload 
SERVER_PID=$!

# Run tests
# pytest tests/

# Kill the server
kill $SERVER_PID
