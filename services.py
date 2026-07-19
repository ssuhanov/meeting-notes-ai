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
