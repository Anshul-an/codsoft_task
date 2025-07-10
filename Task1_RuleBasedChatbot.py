# Task 1 - Rule-Based Chatbot

def chatbot():
    print("🤖 ChatBot: Hello! I’m CodBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("🤖 ChatBot: Goodbye! Have a nice day 😊")
            break

        # Greeting
        elif user_input in ["hi", "hello", "hey"]:
            print("🤖 ChatBot: Hello! How can I help you today?")

        # Asking about the bot
        elif "your name" in user_input:
            print("🤖 ChatBot: I'm CodBot, your friendly rule-based chatbot.")

        # Asking about the weather
        elif "weather" in user_input:
            print("🤖 ChatBot: I'm not connected to the internet, but I hope it’s sunny! ☀️")

        # Asking about the internship
        elif "internship" in user_input or "codsoft" in user_input:
            print("🤖 ChatBot: CODSOFT offers great internships in AI, web dev, and more!")

        # Asking about help
        elif "help" in user_input:
            print("🤖 ChatBot: Sure! You can ask me about the internship, weather, or just chat!")

        # Unknown input
        else:
            print("🤖 ChatBot: I didn’t understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
