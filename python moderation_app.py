import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# 1️⃣ Define banned keywords
# -----------------------------
BANNED_KEYWORDS = ["kill", "hack", "bomb", "terror", "attack"]

# -----------------------------
# 2️⃣ Define system prompt
# -----------------------------
SYSTEM_PROMPT = "You are a safe, helpful AI assistant for health sciences and IT students."

# -----------------------------
# 3️⃣ Input moderation
# -----------------------------
def moderate_input(user_input):
    for word in BANNED_KEYWORDS:
        if word in user_input.lower():
            return False
    return True

# -----------------------------
# 4️⃣ Output moderation
# -----------------------------
def moderate_output(ai_output):
    for word in BANNED_KEYWORDS:
        if word in ai_output.lower():
            ai_output = ai_output.replace(word, "[REDACTED]")
    return ai_output

# -----------------------------
# 5️⃣ Main logic
# -----------------------------
def main():
    user_input = input("Enter your question: ")

    # Step 1: Check input moderation
    if not moderate_input(user_input):
        print("❌ Your input violated the moderation policy.")
        return

    # Step 2: Send request to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ]
    )

    ai_reply = response.choices[0].message.content

    # Step 3: Moderate output
    moderated_output = moderate_output(ai_reply)

    # Step 4: Display result
    print("\n✅ AI Response:")
    print(moderated_output)

if __name__ == "__main__":
    main()
