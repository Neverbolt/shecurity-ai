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

through OpenRouter's OpenAI-compatible API. We have only enabled this model for you, but if you supply your own OpenRouter API key, you can use any model available on there.

## 4. Experiment

Edit `hello_llm.py`, change the user message, and run it again:

```bash
python hello_llm.py
```

When you are done with one part of the exercise you can either continue working in the same file, or copy the file to a new one.

## Keeping your results

This codespace will be deleted after a period of inactivity. If you want to keep your work, you can either:

- Download the files to your local machine.
- Fork the repository and create a new codespace in your fork.
- Use GitHub's "Save" feature to save your work in the cloud.
