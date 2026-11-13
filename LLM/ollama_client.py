import ollama
from config.promts import SYSTEM_PROMPT
def generate_response(prompt:str):
    response=ollama.chat(
        model = "qwen3:8b" ,
        messages=[
            {"role":"user" , "content":prompt}
        ]
    )
    return response["message"]["content"]
