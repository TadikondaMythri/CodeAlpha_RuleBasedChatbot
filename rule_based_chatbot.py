import random
import time
from datetime import datetime

def slow_print(text, delay=0.03):
    """Prints text like typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_time():
    return time.strftime("%I:%M %p")

def get_date():
    return datetime.now().strftime("%A, %d %B %Y")

def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! 😊 How can I assist you today?"
    
    elif "nice to meet you" in user_input:
        return "Me too! 🤝 How can I help you?"
    
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm ChatBuddy! 🤖 — a simple chatbot to assist you!"
    
    elif "time" in user_input:
        return f"Current time is ⏰ {get_time()}"
    
    elif "date" in user_input or "day" in user_input:
        return f"Today is 📅 {get_date()}"
    
    elif "weather" in user_input:
        return "The weather looks pleasant today 🌤️ — perfect for a walk!"
    
    elif "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 💡🐛",
            #"Why don’t bachelors like Git? Because they are afraid to commit! 😂",
            #"Why did the computer go to the doctor? Because it had a virus! 🤒",
            #"Why did the developer go broke? Because they used up all their cache! 💸",
        ]
        return random.choice(jokes)

    elif "happy" in user_input or "great" in user_input or "awesome" in user_input:
        return "That's wonderful! 😄 I'm glad to hear that. Keep smiling!"
    
    elif "sad" in user_input or "upset" in user_input or "low" in user_input:
        return "I'm really sorry to hear that 😔. But just remember — stars can't shine without darkness 🌠"
    
    elif "help" in user_input:
        return (
            "Of course! 😊 I'm here to help you. I can:\n"
            "- Tell you the time or date 🕒\n"
            "- Cheer you up when you're sad 🌈\n"
            "- Tell you a joke 😂\n"
            "- Chat casually and respond to feelings\n"
            "- Do basic calculations like 2 + 2 ➕"
        )

    elif any(op in user_input for op in ['+', '-', '*', '/']):
        try:
            result = eval(user_input)
            return f"The answer is: {result}"
        except:
            return "Oops! I couldn't calculate that. Please check the expression."
        
    elif "bye" in user_input:
        return "Goodbye! 👋 It was nice chatting with you. Have a great day!"
    
    else:
        return "I didn't quite get that 🤔. Maybe try saying 'help'."

def chat():
    slow_print("🤖 Hello! I'm ChatBuddy — your chatbot assistant.", 0.03)
               
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        slow_print("Bot: " + response, 0.01)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chat()
