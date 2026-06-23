import os

from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from fastapi import HTTPException


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
app = FastAPI(title="RAG Project")


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

        # Inspect intermediate result in terminal
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
# -------------------------
# WEEK 7 CODE STARTS HERE
# -------------------------

class QueryRequest(BaseModel):
    question: str
# -------------------------
# Step 3 — Input Validation
# -------------------------

def validate_user_input(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if len(text) < 5:
        raise HTTPException(status_code=400, detail="Question is too short")

    if len(text) > 500:
        raise HTTPException(status_code=400, detail="Question is too long")
# -------------------------
# Step 4 — Output Validation
# -------------------------

def validate_model_output(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=500, detail="AI returned an empty response")

    if len(text) < 10:
        raise HTTPException(status_code=500, detail="AI response is too short")



# -------------------------
# Step 5 — Reviewer Model
# -------------------------
def review_model_output(original_answer: str):
    review_prompt = f"""
You are reviewing an AI-generated response.

Your job:
- If the response is unclear, incomplete, or poorly written, improve it.
- If the response is already good, return it unchanged.

AI response to review:
{original_answer}
"""

    # Use the SAME client style as Week 6
    client = genai.Client(api_key=GEMINI_API_KEY)

    review_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=review_prompt
    )

    return review_response.text

# -------------------------
# Step 6 — New /query Endpoint
# -------------------------

@app.post("/query")
def query_ai(request: QueryRequest):
    validate_user_input(request.question)

    # Use the SAME client style as Week 6
    client = genai.Client(api_key=GEMINI_API_KEY)

    # First model call
    primary_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.question
    )

    raw_answer = primary_response.text

    validate_model_output(raw_answer)

    # Second model call (reviewer)
    review_prompt = f"""
    You are reviewing an AI-generated response.

    Your job:
    - If the response is unclear, incomplete, or poorly written, improve it.
    - If the response is already good, return it unchanged.

    AI response to review:
    {raw_answer}
    """

    review_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=review_prompt
    )

    reviewed_answer = review_response.text

    return {
        "question": request.question,
        "answer": reviewed_answer
    }
