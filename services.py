import os

from click import prompt
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_notes(notes: str):
    prompt = f"""
    Analyze the meeting notes and return ONLY valid JSON.

    The JSON must have exactly this structure:

    {{
        "summary": "...",
        "action_items": [
            "...",
            "..."
        ],
        "decisions": [
            "...",
            "..."
        ],
        "risks": [
            "...",
            "..."
        ]
    }}

    Do not include markdown.
    Do not include explanations.
    Return JSON only.    

    Meeting Notes:

    {notes}
    """

    current_model = "gpt-5.5"
    response = client.responses.create(
        model=current_model,
        input=[
            {"role": "system", "content": "You are an assistant that analyzes meeting notes"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.output_text
