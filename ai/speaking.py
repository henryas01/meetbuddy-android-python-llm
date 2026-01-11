# from ai.ollama import ask_llm
# from ai.prompts import SPEAKING_PROMPT

# def speaking_coach(user_text):
#     prompt = f"""

# User said:
# {user_text}

# """
#     return ask_llm(prompt)

from ai.prompts import SPEAKING_PROMPT
from ai.ollama import ask_llm
from db.repository import save_message, get_conversation

def speaking_coach(session_id: str, user_text: str) -> dict:
    history = get_conversation(session_id)

    context = ""
    for h in history[-6:]:
        context += f"User: {h['user']}\nCoach: {h['ai']}\n"

    prompt = f"""
{SPEAKING_PROMPT}

Conversation:
{context}

User: {user_text}
Coach:
"""

    result = ask_llm(prompt)
    save_message(session_id, user_text, result["response"])

    return {
        "reply": result["response"],
        "processing_time_seconds": result["time"]
    }
