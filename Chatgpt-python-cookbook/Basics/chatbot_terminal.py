
""" 
chatbot_terminal.py
A simple chatbot script you can run in your terminal. 
It stores conversation history in a list and keeps chatting 
until you type "exit" or "quit".

Remarks
-------
API Key. Make sure to store your API key securely.

The script works as follows: 
1. A system message is used to define the assistant's behavior.
2. A while loop handles continuous interaction.
3. Both user and assistant messages are added to the messages list.
4. The full message history is sent to the model on every turn.

"""

import openai
import os

def chat_with_gpt():
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Add user's message to the conversation history
        messages.append({"role": "user", "content": user_input})

        try:
            # Send message history to the model
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Get assistant's reply
            reply = response.choices[0].message.content.strip()
            print("ChatGPT:", reply)

            # Add assistant's reply to the history
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    # Set your API key (recommended from environment variable)
    openai.api_key = os.environ.get("my_openAI_key")

    # Initialize message history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    print("Welcome to ChatGPT Terminal Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    chat_with_gpt()
   
