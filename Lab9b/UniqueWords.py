# Mari Mughdusyan
# CS 119 programming in python
# chapter 9 lab (b)
#
# the program opens a file and counts frequency of all unique words (not including numbers and signs)
# displays the total count of unique words in file


# dictionary for unique words and their frequency
word_counts = {}

with open("text.txt", "r") as file:
    text = file.read()

# replace every non-letter to space
clean_text = ""
for ch in text:
    if ch.isalpha():
        clean_text += ch
    else:
        clean_text += ' '

clean_text = clean_text.lower().split()

for i in clean_text:
    word_counts[i] = word_counts.get(i, 0) + 1

print("Words and their frequencies \n")
for word in sorted(word_counts):
    print(f"{word}: {word_counts[word]}")

print("\nTotal unique words:", len(word_counts))