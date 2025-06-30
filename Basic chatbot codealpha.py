def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what's your name":
        return "I'm ChatBot 1.0!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

print("Welcome to Simple ChatBot!")
print("You can say 'hello', 'how are you', 'what's your name', or 'bye' to exit.")

# Loop until user says "bye"
while True:
    user_input = input("You: ")
    reply = chatbot_response(user_input)
    print("Bot:", reply)
    if user_input.lower() == "bye":
        break


# Welcome to Simple ChatBot!
# You can say 'hello', 'how are you', 'what's your name', or 'bye' to exit.
# You: hello
# Bot: Hi!
# You: how are you
# Bot: I'm fine, thanks!
# You: what's your name
# Bot: I'm ChatBot 1.0!
# You: bye
# Bot: Goodbye!
