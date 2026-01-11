from ai.ollama import ask_llm
from ai.prompts import BASE_PROMPT, PERSONALITY

def evaluate(transcript, mode="IELTS", style="coach"):
    prompt = f"""
{BASE_PROMPT}
Mode: {mode}
Style: {PERSONALITY[style]}

Transcript:
{transcript}

Return:
- Overall band
- Fluency score
- Grammar score
- Vocabulary score
- Pronunciation score
- Feedback
"""
    return ask_llm(prompt)
