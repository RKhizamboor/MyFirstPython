# Program to identify the longest word from an input string

# Initialize variables
totalWords = 0
uniqueWords = []
noOfUniqueWords = 0
longestString = ""
strLength = 0

# Prompt for a File Name
fileName = input("Enter a file name (with complete path):")

try:
    inputFile = open(fileName, mode='r', encoding='utf-8')

# for each line within the input file, get a list of words and iterate each word to find unique/longest word

    for line in inputFile:

        listOfWords = []
        listOfWords = line.split()

        for word in listOfWords:
            totalWords += 1
            if word in uniqueWords:
                continue
            else:
                noOfUniqueWords += 1
                uniqueWords.append(word)
                if len(word) > strLength:
                    longestString = word
                    strLength = len(word)
except FileNotFoundError:
    print("File/Directory not found")
finally:
    if totalWords != 0:
        inputFile.close()

# Alphabetically sort the list of unique words
uniqueWords.sort()

print("Total Words:", totalWords, "Unique Words:", noOfUniqueWords)
print("List of Unique Words", uniqueWords)
print("Longest Word:", longestString, " Str Length:", strLength)