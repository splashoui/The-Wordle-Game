# Read the word list from txt file.

with open("word_list.txt","r") as f:
    valid_words = f.read().split("\n")

