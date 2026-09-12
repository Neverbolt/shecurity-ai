import os

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "qwen/qwen3.8-flash"

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key or api_key == "put-your-key-here":
    raise SystemExit(
        "Missing OPENROUTER_API_KEY.\n"
        "Open the .env tab and paste your workshop API key there."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are my personal assistant for solving cybersecurity CTF challenges.",
        },
        {
            "role": "user",
            "content": "Hello buddy, are we ready?",
        },
    ],
    max_tokens=300,
)

message = response.choices[0].message
print(message.content)
