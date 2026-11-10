import os
from dotenv import load_dotenv
from google import genai
from prompt import build_grading_prompt

def grade_resume(resume_text: str) -> str:
    if not resume_text or not resume_text.strip():
        return "Please paste a resume to grade."

    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "GEMINI_API_KEY is not set. Please check your .env file."
    
    client = genai.Client(api_key=api_key)

    prompt = build_grading_prompt(resume_text)

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )

    return response.output_text
