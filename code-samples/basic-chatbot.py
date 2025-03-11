""" 
basic-chatbot.py
Basic example of interaction with ChatGPT.

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

# Replace 'my_openAI_key'; it is the system variable containing the actual 

# OpenAI API key
openai.api_key = os.environ.get("my_openAI_key")

def chat_with_gpt(prompt):
     # Create a chat completion request using the new endpoint structure.
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    # Extract the assistant's reply from the response.
    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    user_input = input("Enter your message for ChatGPT: ")
    print("ChatGPT is thinking...\n")
    answer = chat_with_gpt(user_input)
    print("ChatGPT:", answer)