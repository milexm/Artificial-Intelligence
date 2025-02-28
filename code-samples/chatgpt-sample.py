import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key ="YOUR_API_KEY"

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    # Extract the assistant's reply from the response
    reply = response.choices[0].message.content.strip()
    return reply

if __name__ == "__main__":
    user_input = input("Enter your message for ChatGPT: ")
    print("ChatGPT is thinking...\n")
    answer = chat_with_gpt(user_input)
    print("ChatGPT:", answer)