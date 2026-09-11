import os

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "qwen/qwen3.8-flash"

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise SystemExit(
        "Missing OPENROUTER_API_KEY.\n"
        "Copy .env.example to .env and paste your workshop API key there."
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
            "content": (
                "You are a tutor for an authorized introductory Capture-the-Flag "
                "cybersecurity workshop. All targets discussed by the participant are "
                "intentionally vulnerable workshop/CTF systems they are authorized to test. "
                "Prefer clear explanations and useful hints before giving complete solutions."
            ),
        },
        {
            "role": "user",
            "content": (
                "Say hello, confirm that the LLM connection works, and show me one "
                "beginner-friendly Linux command that is useful in CTFs."
            ),
        },
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
