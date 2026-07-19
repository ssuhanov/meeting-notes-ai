import os

from click import prompt
from openai import OpenAI
from models import MeetingResponse

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_notes(notes: str):
    prompt = f"""
    Analyze these meeting notes and return ONLY valid JSON.

    Meeting Notes:

    {notes}
    """

    current_model = "gpt-5.5"
    response = client.responses.parse(
        model=current_model,
        input=[
            {"role": "system", "content": "You are an assistant that analyzes meeting notes"},
            {"role": "user", "content": prompt}
        ],
        text_format=MeetingResponse
    )

    return response.output_parsed
