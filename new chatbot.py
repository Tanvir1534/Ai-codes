import nltk
from nltk.chat.util import Chat, reflections

# Define the conversation patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hey there! How can I help?"]),
    
    (r"how are you?", ["I'm doing great, thanks for asking! How about you?", "I'm good, just here to chat!"]),
    
    (r"what is your name?", ["I don't have a personal name, but you can call me Bot.", "I'm just a chatbot!"]),
    
    (r"bye", ["Goodbye! Have a great day!", "See you later!"]),
    
    # Asking for a fun fact
    (r"tell me a fun fact", ["Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!"]),
    
    # Asking about favorite color
    (r"what's your favorite color?", ["I don't have a favorite color, but I think blue is a nice choice!"]),
    
    # Asking the chatbot for advice
    (r"can you give me advice?", ["Sure! Always believe in yourself and take small steps toward your goals."]),
    
    # Asking about food
    (r"what do you like to eat?", ["I don't eat, but I imagine pizza is delicious!"]),
    
    # Responding to "I'm bored"
    (r"i'm bored", ["Oh no! How about we chat? Or I could tell you a joke."]),
    
    # Giving a simple compliment
    (r"you're awesome", ["Thanks! You're pretty awesome too!"]),
    
    # Catch-all pattern for any unrecognized input
    (r"(.*)", ["Sorry, I didn't quite understand that. Can you try asking something else?"]),
]

# Create the chatbot and start the conversation
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
