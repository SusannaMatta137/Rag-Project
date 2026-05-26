# RAG Project

This repository contains my Retrieval-Augmented Generation (RAG) project for the GenAI Secure Coding course.

This project will be built incrementally each week.


## Git Commands Used So Far

- git clone  
- git status  
- git add  
- git commit  
- git push

Week 4 - Understanding Concepts
Environment Variables: 
The app uses load_dotenv() to load values from the .env file.
The Gemini API key is read using os.getenv("GEMINI_API_KEY").

API Key Validation:  
The app checks whether the key exists.
If not, it raises a clear error so the server won’t start without it.

Gemini Configuration:
genai.configure(api_key=GEMINI_API_KEY) sets up the Gemini client.
No Gemini calls are implemented yet.

FastAPI App Setup: 
app = FastAPI() creates the web server.

Health Endpoint: 
The /health endpoint returns a JSON message confirming the server is running and the API key loaded successfully.

Week 4 — Backend Setup Summary
What I Set Up This Week
- Created project files (rag_app.py, .env, requirements.txt, .gitignore)
- Installed FastAPI, Uvicorn, python-dotenv, and Google Gemini libraries
- Created and activated a virtual environment
- Added my Gemini API key to .env
- Ran the FastAPI server successfully

Purpose of rag_app.py
- Loads environment variables using load_dotenv()
- Reads the GEMINI_API_KEY from .env
- Validates that the API key exists
- Configures the Gemini client (no calls yet)
- Creates a FastAPI app
- Provides a /health endpoint to confirm the server is running