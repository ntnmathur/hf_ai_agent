import requests
import json
import os

# Load API token from environment variable
API_TOKEN = os.getenv("HF_API_TOKEN")
if not API_TOKEN:
    raise ValueError("Please set the HF_API_TOKEN environment variable.")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def query_llm(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1000,
            "temperature": 0.1,
            "return_full_text": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    while True:
        user_prompt = input("Ask a question (or 'quit' to exit): ")
        if user_prompt.lower() == "quit":
            break
        response = query_llm(user_prompt+". Only answer this question and nothing else. Response should be less than 500 words.")
        print(f"AI Response: {response.strip()}")