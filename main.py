def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    numWords = wordCount(text)
    letterCount = characterCount(text)
    numLetters = countedLetters(letterCount)
    niceReport = prettyReport(letterCount)
    print("*-*-* BOOT.DEV BOOK BOT REPORT *-*-*")
    print(f"Path to file chosen: {bookPath}")
    print(f"Total number of words in {bookPath}: {numWords}")
    print(f"Total number of letters in {bookPath}: {numLetters}")
    for line in niceReport:
        print(line)


def getText(path):
    with open(path) as j:
        return j.read()


def wordCount(file):
    words = file.split()
    wordCount = len(words)
    return wordCount

def countedLetters(charList):
    totalLetters = 0
    for c in charList:
        totalLetters += charList[c]
    return totalLetters
    

def characterCount(file):
    charCountDict = {}
    for letter in file:
        if letter.isalpha():
            letter = letter.lower()
            if letter in charCountDict:
                charCountDict[letter] += 1
            else:
                charCountDict[letter] = 1
    return charCountDict


def prettyReport(charCount):
    reportList = []
    sortLetters = dict(sorted(charCount.items()))
    for c in sortLetters:
        reportList.append(f"The letter {c} appeared in this text {sortLetters[c]} times.")
    return reportList 


main()
