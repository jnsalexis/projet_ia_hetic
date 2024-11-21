from openai import ChatCompletion

# API Configuration (remplacez par les paramètres de votre choix)
API_KEY = "XXX"

def query_llm(prompt: str, temperature: float = 0.7) -> str:
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=200,
    )
    return response['choices'][0]['message']['content']
