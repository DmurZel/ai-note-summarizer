import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    if not text:
        return "No text provided to summarize."

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight model for summaries
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize this: {text}"}
        ],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()