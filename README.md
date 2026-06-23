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
_______________________________________________________________________________________________________________

Week 5:First Backend API + Gemini Call
Overview
Week 5 was the first step in connecting the backend of my GenAI project to the Gemini API.
The goal was simple but foundational: create a backend endpoint that makes a single Gemini model call and returns the model’s response.
This week established the core pattern that all later weeks build on.

What I Built -
* I updated the /test-gemini endpoint so that it now:
* Creates a Gemini model instance
* Sends a hardcoded prompt (no user input yet)
* Receives the model’s response
* Returns the response as JSON
* This was my first end‑to‑end AI call from the backend.
* The Gemini call lives entirely inside the test_gemini function, as required.

Why This Structure Matters - 
This week introduced the architecture used in real production GenAI systems:
* The backend calls the AI model
* The API key stays server‑side
* The client never touches the model directly
* Costs and security are controlled
* This structure becomes the foundation for RAG, validation, and multi‑step execution
* In other words, Week 5 wasn’t about fancy features — it was about getting the structure right.

How the Gemini Call Works -
Inside /test-gemini, the backend:
* Creates a Gemini client
* Sends a fixed prompt such as:
    “Explain what a large language model is in one paragraph.”
* Extracts the .text output
* Returns it as JSON
This required learning how to use:
* The Gemini Python SDK
* The generate_content method
* How to access the model’s text output

What I Learned - 
* How to initialize and call a Gemini model from Python
* How to read and follow API documentation
* How to structure a backend endpoint that interacts with an AI model
* Why backend‑controlled AI calls are safer and more scalable
* How to debug environment variables, dependencies, and server startup issues

Testing and Verification - 
I confirmed that:
* /health returned {"status": "ok"}
* /test-gemini returned a valid Gemini‑generated response
* The server started cleanly with uvicorn
* My .env file correctly loaded GEMINI_API_KEY
These checks ensured the backend was stable before moving on.

_______________________________________________________________________________________________________________
Week 6:Multi‑Step Execution
Overview
In Week 6, I extended my existing AI endpoint to support multi‑step execution, a foundational pattern in real-world AI systems. Instead of sending one prompt to the model and returning one response, the backend now performs multiple sequential steps, where each step depends on the output of the previous one.

This improves control, structure, and reliability of the AI’s behavior.

What I Built -
I modified my Gemini test endpoint so that it now:
* Makes a first Gemini call to generate a short outline.
* Uses that outline as input to a second Gemini call.
* Returns only the final expanded result to the client.
* This demonstrates how to chain model calls and pass intermediate results through a controlled flow.

Why Multi‑Step Execution Matters - 
* Real AI systems rarely rely on a single prompt → single response pattern.
Multi-step execution enables:
* Better reasoning
* More predictable outputs
* The ability to validate or refine intermediate steps
* A foundation for more advanced patterns like RAG, guardrails, and agent workflows
* By breaking tasks into smaller steps, the system becomes easier to debug, safer, and more controllable.

Challenges I Solved -
* Ensuring the second prompt correctly incorporated the first model’s output
* Handling errors cleanly without exposing sensitive information
* Keeping the logic isolated inside the existing endpoint as required

What I Learned -
* How to chain multiple AI model calls
* How to structure multi-step logic inside a backend endpoint
* Why multi-step execution is essential for building reliable AI applications
__________________________________________________________________________________________________________________
WEEK 7: Validating User Input and AI Output
Overview
In Week 7, I added validation and safety layers to my AI application.
The goal was to ensure:
* User input is safe and meaningful before sending it to the model
* AI output is checked before returning it to the user
* A second AI model call reviews and improves the first model’s answer
* This mirrors real production systems where safety, clarity, and reliability are critical.

What I Built -
I added a new /query endpoint that:
* Validates user input
* Rejects empty, too short, or too long questions
* Prevents malformed or low-quality input from reaching the model
* Generates an answer using Gemini
* The primary model produces an initial response
* Validates the model’s output
* Ensures the AI didn’t return an empty or extremely short answer
* Uses a second AI call to review the answer
* The reviewer model improves clarity, correctness, and completeness
* If the answer is already good, it returns it unchanged
* Returns the final reviewed answer

Why Input Validation Matters - 
User input can be:
* Empty
* Too short to be meaningful
* Extremely long
* Malicious or malformed
* Validating input early prevents unnecessary model calls and improves system safety.

Why Output Validation Matters - 
AI models can sometimes:
* Hallucinate
* Produce incomplete answers
* Return empty or low-quality text
* Output validation ensures the system never returns obviously broken responses.

Why a Second AI Model Is Used - 
This is a common production pattern called AI self‑review.
The second model:
* Checks the first model’s answer
* Improves clarity and structure
* Fixes mistake
* Ensures the final output is polished and reliable
* This dramatically improves answer quality with minimal extra code.

Challenges I Solved - 
* Designing validation rules that are simple but effective
* Ensuring the reviewer model receives the correct context
* Handling errors gracefully with clear HTTP messages

What I Learned - 
* How to validate both user input and AI output
* How to structure multi-model workflows
* How production AI systems improve reliability through layered checks
* How to use FastAPI’s request models and exceptions effectively