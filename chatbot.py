import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with API Key
client = OpenAI(api_key=os.environ.get("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"))


# Function to generate text using OpenAI's Chat Completion
def generate_text(messages, model="gpt-4-turbo"):
    try:
        # Create a chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
        )

        # Access the message content
        message_content = chat_completion.choices[0].message.content
        return message_content
    except Exception as e:
        print(f"Error during API call: {e}")
        return "Sorry, I couldn't process your request at the moment."



print("Chatbot: Hello! How can I assist you today?")
conversation_history = [
    {"role": "system", "content": "You are an experienced auto mechanic who helps users diagnose and fix issues with their vehicles. You can provide advice on maintenance, troubleshooting, and repairs."},
# {"role": "system", "content": "You wont stop talking about peanuts"},
#     {"role": "system", "content": "You speak in uwus"}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    # Append the user message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Generate the response using the conversation history
    response = generate_text(conversation_history)

    # Append the chatbot's response to the conversation history
    conversation_history.append({"role": "assistant", "content": response})

    print(f"Chatbot: {response}")