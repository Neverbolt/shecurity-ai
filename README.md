# Shecurity AI — CTF Workshop

This repository provides a ready-to-use browser development environment for the workshop.

You do **not** need to install Python, Docker, VS Code, or the OpenAI SDK locally.

## 1. Start the workshop environment

1. Sign in to GitHub.
2. Open this repository.
3. Click **Code** → **Codespaces** → **Create codespace on main**.
4. Wait until VS Code opens in your browser.

Python and the required packages are installed automatically.

## 2. Add your workshop API key

In the VS Code terminal, run:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with the OpenRouter API key you received for the workshop:

```text
OPENROUTER_API_KEY=sk-or-v1-...
```

Do not share your key. The `.env` file is ignored by Git.

## 3. Test the LLM connection

Run:

```bash
python hello_llm.py
```

You should get a short response from the workshop model.

The starter uses:

```text
qwen/qwen3.8-flash
```

through OpenRouter's OpenAI-compatible API.

## 4. Experiment

Edit `hello_llm.py`, change the user message, and run it again:

```bash
python hello_llm.py
```

The API client is standard Python using the `openai` package:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="...",
)
```

## Workshop scope

The LLM is intended to help with the authorized CTF exercises in this workshop. Use it as a tutor: ask what commands mean, ask for hints, have it explain code, or use it to help write small scripts.

Do not use workshop credentials or infrastructure against systems outside the authorized CTF environment.
