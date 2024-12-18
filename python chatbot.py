import nltk
from nltk.chat.util import Chat, reflections

# Define some basic conversation patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm fine, how about you?"]),
    (r"what is your name?", ["I'm a chatbot. You can call me Bot."]),
    (r"bye", ["Goodbye!", "See you later!"]),
    (r"(.*)", ["I'm not sure how to respond to that."])
]

# Create a Chat object with the patterns and reflections
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
