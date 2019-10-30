# Determine the longest word within an Input string

# Get input from stdin
iString = input("Enter a string:")

# Initialize a list
listOfWords = []
# Split the string into individual words

iString_words = iString.split()

for word in iString_words:
    listOfWords.append(word)

print(listOfWords)