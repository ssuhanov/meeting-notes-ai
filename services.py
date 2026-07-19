import os

from click import prompt
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_notes(notes: str):
    prompt = f"""
    You are an assistant that analyzes meeting notes

    Return:

    - Summary
    - Action Items
    - Decisions
    - Risks

    Meeting Notes:

    {notes}
    """

    current_model = "gpt-5.5"
    response = client.chat.completions.create(
        model=current_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
