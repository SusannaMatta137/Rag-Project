import os

from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai
#import google.generativeai as genai
#from google import genai


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
# ---> genai.configure(api_key=GEMINI_API_KEY)

#genai.configure(api_key=GEMINI_API_KEY)

# Create FastAPI app
app = FastAPI(title="RAG Project - Week 4 Skeleton")


@app.get("/health")
def health_check():
    """Simple health endpoint to confirm the server is running and the key is loaded."""
    return {
        "status": "ok",
        "message": "Server is running and Gemini API key is configured.",
    }
    
#def test_gemini():
    #try:
        # Create a Gemini model
        #model = genai.GenerativeModel("gemini-1.5-flash")

        #model = genai.GenerativeModel("gemini-1.5-flash")
       # model = genai.GenerativeModel("gemini-pro")
        #model = genai.GenerativeModel("models/text-bison-001")


        # Hardcoded prompt
       # prompt = "Explain what a large language model is in one paragraph."

        # Call Gemini
      #  response = model.generate_content(prompt)

        # Extract text
      #  output_text = response.text

        # Return JSON
       # return {"response": output_text}

  #  except Exception as e:
      #  raise RuntimeError(f"Gemini test failed: {str(e)}")

#def test_gemini():
 #   try:
  #      client = genai.Client(api_key=GEMINI_API_KEY)

   #    response = client.models.generate_content(
    #   model="gemini-3.5-flash",
     #  contents="Explain how AI works in a few words"
#)

 #       return {"response": response.text}

  #  except Exception as e:
   #     raise RuntimeError(f"Gemini test failed: {str(e)}")

   # from google import genai
#from google import genai
#import os

@app.get("/test-gemini")
def test_gemini():
    try:
        # Create Gemini client
        client = genai.Client(api_key=GEMINI_API_KEY)

        # Hardcoded prompt
        prompt = "Explain how AI works in a few words."

        # Generate response
       # response = client.models.generate_content(
           # model="gemini-1.5-flash",
           # contents=prompt
       # )
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt 
            )

        return {"response": response.text}

    except Exception as e:
        raise RuntimeError(f"Gemini test failed: {str(e)}")
#@app.get("/test-gemini")
#def run_test_gemini():
 #   return test_gemini()
