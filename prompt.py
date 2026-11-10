def build_grading_prompt(resume_text: str) -> str:
    """Build the instruction Gemini will receive with a resume."""
    return f"""
You are a helpful career coach giving constructive feedback on a student resume.

Give an overall score out of 100. Consider:
- technical content
- experience and projects
- specificity and measurable impact
- clarity and organization

Include these headings in your response:
## Overall Score
## Key Strengths
## Areas for Improvement
## Actionable Recommendations

Be kind, specific, and concise. Do not invent facts that are not in the resume.

Resume to grade:
---
{resume_text}
---
""".strip()
