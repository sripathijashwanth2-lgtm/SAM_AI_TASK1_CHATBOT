print("🤖 Welcome to Rule-Based Chatbot!")
print("Type 'bye' to exit the chatbot.")
print("-----------------------------------")

while True:
    user_input = input("You: ").lower().strip()

    # Greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! 👋 How can I help you?")

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a Rule-Based AI Chatbot.")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! 😊 Thanks for asking.")

    # Help
    elif "help" in user_input:
        print("Bot: I can answer greetings, basic questions, and simple queries.")

    # What can you do
    elif "what can you do" in user_input or "your capabilities" in user_input:
        print("Bot: I can respond to greetings, answer basic questions, and provide simple information.")

    # Thanks
    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome! 😊")

    # Creator
    elif "who created you" in user_input or "who made you" in user_input:
        print("Bot: I was created as a Rule-Based Chatbot project.")

    # Internship
    elif "internship" in user_input:
        print("Bot: This chatbot is developed as part of an AI internship task.")

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see what I can do.")