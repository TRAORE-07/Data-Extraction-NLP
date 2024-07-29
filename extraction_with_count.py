# Alphabets, words and sentences extraction and count in a given text.
import re

text = input("Text: ")

# Alphabet counts (using set and dictionary)
alpha_counts = {}
pattern = re.findall(r"[a-zA-Z]", text)
for char in pattern:
    alpha_counts[char.upper()] = alpha_counts.get(char.upper(), 0) + 1

# Print alphabet counts
print("Alphabets:")
for alphabet, count in alpha_counts.items():
    print(f"{alphabet}: {count}")

# Word extraction (separated by spaces)
words_counts = {}
words_pattern = re.findall(r"\b\w+\b", text)
for wrd in words_pattern:
    words_counts[wrd] = words_counts.get(wrd, 0) + 1

# Print the word counts
print("\nWords:")
for words, count in words_counts.items():
    print(f"{count}: {words}")

# Sentence extraction (any sequence of characters followed by punctuation)
sentences = re.findall(r".+?[.!?]", text)

# Print indexed sentences
print("\nSentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}: {sentence}")