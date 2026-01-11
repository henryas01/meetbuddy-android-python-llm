# import requests
# import time

# list of efficient models for speaking and other tasks: phi4-mini gemma3:4b mistral
# list of efficient models for imaging: llava-llama3 gemma3:4b
# list of efficient models for Math and programming: llava-llama3 still research
  # list of available llama3 (Meta) phi3 phi4-mini gemma3:1b mistral gemma3:4b (Gemini mini)  llava-llama3 gemma3n:e4b

# def ask_llm(prompt: str) -> dict:
#     start_time = time.perf_counter()

#     r = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": MODEL,
#             "prompt": prompt,
#             "stream": False
#         },
#         timeout=(10, 180)
#     )

#     end_time = time.perf_counter()

#     return {
#         "response": r.json()["response"],
#         "processing_time": round(end_time - start_time, 2)  # detik
#     }


# import requests
# import time

# MODEL = "phi4-mini"
# OLLAMA_URL = "http://localhost:11434/api/generate"

# def ask_llm(prompt: str) -> dict:
#     start = time.perf_counter()

#     r = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": MODEL,
#             "prompt": prompt,
#             "stream": False
#         },
#         timeout=(10, 180)
#     )

#     return {
#         "response": r.json()["response"],
#         "time": round(time.perf_counter() - start, 2)
#     }


import requests, time

OLLAMA_URL = "http://localhost:11434/api/generate"

def chat(prompt: str):
    start = time.time()

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi4-mini",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response = r.json()["response"]
    return response, round(time.time() - start, 2)
