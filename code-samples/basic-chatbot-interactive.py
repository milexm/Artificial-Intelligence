""" 
basic-chatbot-interactive.py
Basic example of interactive chatbot that interacts with ChatGPT.
The bot continuously prompts for user input until the user types "exit."
Real-time Interaction: Each user prompt is sent to ChatGPT, 
and its response is displayed immediately.

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
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        answer = chat_with_gpt(user_input)
        print("ChatGPT:", answer)
