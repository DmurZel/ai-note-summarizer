import os
from openai import OpenAI # Ensure you have the OpenAI Python SDK installed: pip install openai


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set. Please set it to use the OpenAI client.")

client = OpenAI(api_key=api_key) # Initialize OpenAI client with API key from environment variable


# Function to summarize text using OpenAI's GPT model
# Uses a lightweight model for efficiency
# Limits the summary to 100 tokens
# Returns a summary string
# Handles empty input gracefully
# Example usage:
# summary = summarize_text("Long text to summarize...")
# print(summary)
# Note: Ensure OPENAI_API_KEY is set in your environment variables
def summarize_text(text: str) -> str: # Summarize the provided text
    if not text:
        return "No text provided to summarize."

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight model for summaries 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."}, # System prompt to guide the model
        ],
        max_tokens=100 # Limit the summary to 100 tokens
    )

    return response.choices[0].message.content.strip() # Return the summary from the response