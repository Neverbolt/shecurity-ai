# Shecurity AI — CTF Workshop

This repository provides a ready-to-use browser development environment for the workshop.

You do **not** need to install Python, Docker, VS Code, or the OpenAI SDK locally.

## 1. Start the workshop environment

1. Sign in to GitHub.
2. Open this repository.
3. Click **Use this template** → **Open in a codespace**.
4. Wait until VS Code opens in your browser.

Python and the required packages are installed automatically. The workshop also creates a local `.env` file and opens `.env` plus `hello_llm.py` for you.

## 2. Add your workshop credentials

Open the `.env` tab. The CTFd URL and workshop category are already configured.

Replace these three placeholders with the credentials you received for the workshop:

- `OPENROUTER_API_KEY` — your workshop LLM API key
- `CTFD_USERNAME` — your CTFd player username
- `CTFD_PASSWORD` — your CTFd player password

Do not share these credentials. The `.env` file is ignored by Git, and a pre-commit hook blocks accidental commits of OpenRouter keys, CTFd passwords, and dotenv files.

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

## 4. CTFd tools available to the LLM

`hello_llm.py` exposes three local tools to the model:

- `get_challenge_description` — load the visible description and metadata for a challenge
- `spawn_challenge` — start or reuse your per-user challenge instance
- `submit_flag` — submit a candidate flag to CTFd

The CTFd username and password stay local in `.env`; they are used by `ctf.py` to log in and are not sent to the LLM.

A challenge can be selected by workshop number, by a case-insensitive name substring, or by a raw CTFd challenge id.

For example, change the user message in `hello_llm.py` to something like:

```text
Get the description for challenge 3 and start my instance.
```

Then run:

```bash
python hello_llm.py
```

The model can call the CTFd tools automatically when needed.

## 5. Experiment

Edit the user message in `hello_llm.py` and run it again:

```bash
python hello_llm.py
```

When you are done with one part of the exercise, you can continue working in the same file or copy it to a new one.

## Keeping your results

A codespace created from the template is initially just your cloud workspace. If you want to keep your work permanently, use **Publish to GitHub** from the Source Control view in VS Code. GitHub will create a repository in your account containing your work.

You can also download individual files if you prefer.
