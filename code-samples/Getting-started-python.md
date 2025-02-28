# Getting Started with Python <!-- omit from toc -->

This article shows how to use **Python** to interact with **OpenAI**, specifically **ChatGPT**.

- [1. Introduction](#1-introduction)
- [2. Prerequisites](#2-prerequisites)
- [3. Setup and Installation](#3-setup-and-installation)
- [4. Writing Your First Python Script](#4-writing-your-first-python-script)
- [5. Running the Script](#5-running-the-script)
- [6. Next Steps and Best Practices](#6-next-steps-and-best-practices)
- [7. References](#7-references)

## 1. Introduction

ChatGPT, powered by models like GPT-3.5 or GPT-4, is a versatile AI that can understand and generate human-like text. By using Python, you can build applications that interact with ChatGPT for tasks like chatbots, content generation, or even code assistance.

## 2. Prerequisites

- Python 3.7 or higher: Ensure you have an up-to-date version of Python.
- An OpenAI account: You need to sign up on OpenAI's website and obtain an API key.
- Basic familiarity with Python: Knowledge of variables, functions, and handling packages will be helpful.

## 3. Setup and Installation

- Obtain an API Key
  - Sign up or log in to your OpenAI account.
  - Navigate to the API section in your account settings.
  - Generate a new API key. Save this key securely, as you'll need it to authenticate your requests.
- Install the OpenAI Python Package
  - Open your terminal or command prompt and run:

    ``` bash
        pip install openai
    ```

## 4. Writing Your First Python Script

Create a new Python file e.g., [chatgpt-sample.py](chatgpt-sample.py).

The following is a snippet of the code sample.

``` python

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

```

## 5. Running the Script

Open your terminal, navigate to the directory containing your script, and run:

``` bash
    python chatgpt_example.py
```

Type your query when prompted, and the script will display ChatGPT's response.
The following is an example of the exchange between ChatGPT and the user:

> Enter your message for ChatGPT: Goodmorning in Italian
ChatGPT is thinking...
> ChatGPT: "Buongiorno" in Italian! How can I assist you today?

## 6. Next Steps and Best Practices

- **Error Handling**. Enhance your script by adding try-except blocks to manage potential API errors.
- **Experiment with Parameters**. Explore other parameters in the API (such as temperature for controlling randomness or max_tokens for response length).
- **Secure Your API Key**. Avoid hardcoding the API key in your script. Instead, consider using environment variables or secure vaults.
- **Read the Documentation**. For advanced usage and further customization, refer to the OpenAI API documentation.

## 7. References

- [OpenAI Platform](https://platform.openai.com/settings/organization/general)
- [ChatGPT](https://chatgpt.com/)
