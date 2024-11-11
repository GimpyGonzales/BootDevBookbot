def main():
    bookPath = "books/frankenstein.txt"
    text = printText(bookPath)
    countWords = wordCount(bookPath)
    print(f"{countWords} words found in document in path {bookPath}")

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

main()
