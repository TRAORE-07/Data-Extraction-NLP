# Alphabets, words and sentences extraction in a given text.
import re

user_input = input("Enter your text: ")

# Alphabet extraction (a-z and A-Z)
alphabets = re.findall(r"[a-zA-Z]", user_input)
print("Alphabets: ", alphabets)

# Word extraction (separated by spaces)
words = re.findall(r"\b\w+\b", user_input)
print("Words: ", words)

# Sentence extraction (any sequence of characters followed by punctuation)
sentences = re.findall(r".+?[.!?]", user_input)
print("Sentences: ")
for sentence in sentences:
    print(sentence)