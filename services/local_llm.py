import ollama

MODEL = "qwen2.5-coder:1.5b"

def generate(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3, "num_predict": 1400}
    )

    return response["message"]["content"]
