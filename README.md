AI Resume Grader
A web app that takes a pasted plain-text resume and returns structured feedback from Google's Gemini API: an overall score out of 100, key strengths, areas for improvement, and actionable recommendations.
Built from a starter project from my school's AI club workshop. The Gradio interface (app.py) was provided as part of the starter. I implemented the Gemini integration in ai.py.

How it works

Resume text -> Gradio UI (app.py) -> grade_resume() (ai.py) -> Gemini API -> feedback shown in the UI
app.py: Gradio interface with a text box and a "Grade Resume" button
ai.py: loads the API key from a .env file, validates the input, sends the prompt to Gemini, and returns the response
prompt.py: builds the grading prompt, including the scoring criteria (technical content, experience and projects, measurable impact, clarity), the required response headings, and an instruction not to invent facts that aren't in the resume


Setup

You need Python 3.9+ and a Gemini API key from Google AI Studio.
bash
python3 -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Create a file named .env in the project folder:

GEMINI_API_KEY=your_key_here


Run

bash
python app.py
Open the local URL printed in the terminal (usually http://127.0.0.1:7860) and paste in a resume.


Tech

Python, Gradio, Google Gemini API (google-genai), python-dotenv


Possible extensions

Compare a resume against a job description
Per-category scores
PDF upload
Saving past results


Credits

Starter project from my school's AI club workshop.
