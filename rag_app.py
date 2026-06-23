import os

from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai

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

# Create FastAPI app
app = FastAPI(title="RAG Project - Week 4 Skeleton")


@app.get("/health")
def health_check():
    """Simple health endpoint to confirm the server is running and the key is loaded."""
    return {
        "status": "ok",
        "message": "Server is running and Gemini API key is configured.",
    }
    

@app.get("/test-gemini")
def test_gemini():
    try:
        # Create Gemini client
        client = genai.Client(api_key=GEMINI_API_KEY)

        # STEP 1: Generate an outline
        outline_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Create a 3-point outline explaining what a large language model is."
        )

        outline = outline_response.text

        # Optional: inspect intermediate result in terminal
        print("Generated Outline:")
        print(outline)

        # STEP 2: Expand the outline into a paragraph
        final_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Use the outline below to write one short explanatory paragraph.

            Outline:
            {outline}
            """
        )

        return {"response": final_response.text}

    except Exception as e:
        raise RuntimeError(f"Gemini multi-step test failed: {str(e)}")
