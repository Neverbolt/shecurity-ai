import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from ctf import CTFError, get_challenge_description, spawn_challenge, submit_flag

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

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "spawn_challenge",
            "description": (
                "Start a per-user CTFd challenge instance, or return the existing "
                "instance if it is already running."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "challenge": {
                        "type": "string",
                        "description": (
                            "Challenge selector: workshop number such as '3', "
                            "case-insensitive name substring, or raw CTFd id."
                        ),
                    }
                },
                "required": ["challenge"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_challenge_description",
            "description": "Get the visible CTFd description and metadata for a challenge.",
            "parameters": {
                "type": "object",
                "properties": {
                    "challenge": {
                        "type": "string",
                        "description": (
                            "Challenge selector: workshop number, name substring, "
                            "or raw CTFd id."
                        ),
                    }
                },
                "required": ["challenge"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "submit_flag",
            "description": "Submit a candidate flag for a challenge to CTFd.",
            "parameters": {
                "type": "object",
                "properties": {
                    "challenge": {
                        "type": "string",
                        "description": (
                            "Challenge selector: workshop number, name substring, "
                            "or raw CTFd id."
                        ),
                    },
                    "flag": {
                        "type": "string",
                        "description": "Candidate flag to submit.",
                    },
                },
                "required": ["challenge", "flag"],
                "additionalProperties": False,
            },
        },
    },
]

TOOL_FUNCTIONS = {
    "spawn_challenge": spawn_challenge,
    "get_challenge_description": get_challenge_description,
    "submit_flag": submit_flag,
}


def execute_tool(tool_call) -> str:
    """Execute one model-requested CTFd tool and return JSON to the model."""
    name = tool_call.function.name
    function = TOOL_FUNCTIONS.get(name)
    if function is None:
        return json.dumps({"ok": False, "error": f"Unknown tool: {name}"})

    try:
        arguments = json.loads(tool_call.function.arguments or "{}")
        result = function(**arguments)
        return json.dumps({"ok": True, "result": result})
    except (CTFError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return json.dumps({"ok": False, "error": str(exc)})
    except Exception as exc:
        return json.dumps({"ok": False, "error": f"Tool failed: {exc}"})


messages = [
    {
        "role": "system",
        "content": (
            "You are my personal assistant for solving authorized cybersecurity "
            "CTF challenges. You have tools to read a challenge description, start "
            "a per-user challenge instance, and submit candidate flags. Use those "
            "tools when they are useful. Never ask the user to reveal their CTFd "
            "password or OpenRouter API key; those credentials are handled locally."
        ),
    },
    {
        "role": "user",
        "content": "Hello buddy, are we ready?",
    },
]

for _ in range(8):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        max_tokens=700,
    )

    message = response.choices[0].message
    messages.append(message.model_dump(exclude_none=True))

    if not message.tool_calls:
        print(message.content or "")
        break

    for tool_call in message.tool_calls:
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": execute_tool(tool_call),
            }
        )
else:
    raise SystemExit("Too many consecutive tool calls; stopping.")
