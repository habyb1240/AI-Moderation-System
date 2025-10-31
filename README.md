# 🧠 AI Moderation System

This project implements a **basic AI moderation system** using the **OpenAI API**.  
It checks both **user inputs** and **AI outputs** to ensure that harmful or disallowed content is filtered out before being processed or displayed.

---

## ⚙️ Features
- Input moderation — blocks user prompts containing banned keywords.
- Output moderation — replaces disallowed words in AI responses with `[REDACTED]`.
- Uses **OpenAI GPT model** to generate intelligent responses.
- Designed for **students in health sciences and computer information technology**.

---

## 🧩 Functional Requirements

### 1. System Prompt
Defines the AI’s role and safe behavior:
> “You are a safe, helpful AI assistant for health sciences and IT students.”

### 2. User Prompt
Collected dynamically from the user through input.

### 3. API Call
A POST request is sent to the OpenAI API endpoint with moderation logic.

### 4. Moderation Logic
- **Input moderation:** Reject prompt if it includes banned keywords (e.g., *kill*, *hack*, *bomb*).
- **Output moderation:** Replace banned words in AI responses with `[REDACTED]`.

5. Output
Displays either:
- The moderated AI response, or  
- `"Your input violated the moderation policy."`

---

🧰 Installation and Setup

 1. Install Python
Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Ensure you check **“Add Python to PATH”** during installation.

2. Install Dependencies
Open Command Prompt and run:
```bash
pip install openai
