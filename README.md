# Shecurity AI — CTF Workshop

This repository provides a ready-to-use browser development environment for the workshop.

You do **not** need to install Python, Docker, VS Code, or the OpenAI SDK locally.

## 1. Start the workshop environment

1. Sign in to GitHub.
2. Open this repository.
3. Click **Use this template** → **Open in a codespace**.
4. Wait until VS Code opens in your browser.

Python and the required packages are installed automatically. The workshop also creates a local `.env` file for your API key and opens the important files for you.

## 2. Add your workshop API key

Open the `.env` tab and replace the placeholder with the OpenRouter API key you received for the workshop:

```text
OPENROUTER_API_KEY=sk-or-v1-...
```

Do not share your key. The `.env` file is ignored by Git, and a pre-commit hook blocks accidental commits of OpenRouter keys.

## 3. Test the LLM connection

Run this in the VS Code terminal:

```bash
python hello_llm.py
```

You should get a short response from the workshop model.

The starter uses:

```text
qwen/qwen3.8-flash
```

through OpenRouter's OpenAI-compatible API. We have only enabled this model for the workshop key. If you supply your own OpenRouter API key, you can use any model available to your account.

## 4. Experiment

Edit `hello_llm.py`, change the user message, and run it again:

```bash
python hello_llm.py
```

When you are done with one part of the exercise, you can continue working in the same file or copy it to a new one.

## Keeping your results

A codespace created from the template is initially just your cloud workspace. If you want to keep your work permanently, use **Publish to GitHub** from the Source Control view in VS Code. GitHub will create a repository in your account containing your work.

You can also download individual files if you prefer.
