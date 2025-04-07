
""" 
teschat_basic.py
A basic Python script that sends a message to ChatGPT and prints the response.


Remarks
-------
API Key. Make sure to set your API key securely.
Endpoint Call. We call openai.chat.completions.create() with:
    model: Which model to use (e.g., "gpt-3.5-turbo").
    messages: A list that defines the conversation 
    context (a system message and a user message).
Response Parsing. The assistant's reply is accessed from the 
response object.
"""

import openai
import os

# Set your API key (recommended from environment variable)
openai.api_key = os.environ.get("my_openAI_key")

# Create a message to send
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

# Send the message to ChatGPT
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Extract and print the assistant's reply
reply = response.choices[0].message.content
print("ChatGPT:", reply)

