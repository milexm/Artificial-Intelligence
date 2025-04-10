
""" 
test_api.py
Basic example of interaction with ChatGPT.

Remarks
-------
API Key. Make sure to store
your API key securely.
Endpoint Call. We call openai.chat.completions.create() with:
    model: Which model to use (e.g., "gpt-3.5-turbo").
    messages: A list that defines the conversation 
    context (a system message and a user message).
Response Parsing. The assistant's reply is accessed from the 
response object.
"""

import openai
import os

# Option 1: Get the API key from an environment variable
openai.api_key = os.environ.get("my_openAI_key")

# Option 2: Directly assign your API key (use only for testing)
# openai.api_key = "your_secret_key_here"

def test_chat():
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is your name?"},
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    reply = test_chat()
    print("ChatGPT says:", reply)
