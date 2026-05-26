import os

from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Read the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    # Fail clearly if the key is missing
    raise RuntimeError(
        "GEMINI_API_KEY is not set. "
        "Create a .env file in the project root and add GEMINI_API_KEY=your_api_key_here"
    )

# Configure Gemini (no actual calls yet)
genai.configure(api_key=GEMINI_API_KEY)

# Create FastAPI app
app = FastAPI(title="RAG Project - Week 4 Skeleton")


@app.get("/health")
def health_check():
    """Simple health endpoint to confirm the server is running and the key is loaded."""
    return {
        "status": "ok",
        "message": "Server is running and Gemini API key is configured.",
    }
    
def test_gemini():
    try:
        # Create a Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Hardcoded prompt
        prompt = "Explain what a large language model is in one paragraph."

        # Call Gemini
        response = model.generate_content(prompt)

        # Extract text
        output_text = response.text

        # Return JSON
        return {"response": output_text}

    except Exception as e:
        raise RuntimeError(f"Gemini test failed: {str(e)}")
