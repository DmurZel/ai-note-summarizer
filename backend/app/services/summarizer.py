import openai
import os

# Make sure you set your API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str) -> str:
    if not text.strip():
        return "No text provided to summarize."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text:\n{text}",
        max_tokens=60
    )
    return response.choices[0].text.strip()