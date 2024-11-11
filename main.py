def main():
    bookPath = "books/frankenstein.txt"
    letterCount = characterCount(bookPath)
    print(f"Please see below for count of all letters in file in path {bookPath}")
    print(letterCount)

def printText(path):
    with open(path) as f:
        fileContents = f.read()
        return fileContents

def wordCount(path):
    with open(path) as f:
        fileContents = f.read()
        words = fileContents.split()
        wordCount = len(words)
        return wordCount

def characterCount(path):
    charCountDict = {}
    with open(path) as f:
        fileContents = f.read()
        for letter in fileContents:
            if letter.isalpha():
                letter = letter.lower()
                if letter in charCountDict:
                    charCountDict[letter] += 1
                else:
                    charCountDict[letter] = 1
        return charCountDict
    
main()
