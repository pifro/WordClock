from __future__ import print_function
import config


class NoLayoutError(Exception):
    pass

class Layout:

    rows = ""
    numRows = 0
    rowSize = 0

    
    def __init__(self, numRows, rowSize):
        self.numRows = numRows
        self.rowSize = rowSize

        for i in range(numRows):
            for j in range(rowSize):
                self.rows += "_"
            self.rows += "|"

    def addLettersIfNeeded(self, letters, position=0):

        #  print("*** Adding " + letters + " *** - " + str(position))

        subset, index = self.findBiggestSubsetAndIndex(letters, position)

        if index == - 1:
            self.appendLetters(letters)

        else:
            remainingLetters = letters[len(subset):]

            if len(remainingLetters) == len(letters):
                raise RuntimeError(
                    'Recursion! :' + letters + '/' + remainingLetters)

            if len(remainingLetters) > 0:
                self.addLettersIfNeeded(remainingLetters, position + index + 1)

    def findBiggestSubsetAndIndex(self, letters, position):
        maxIndex = -1
        maxSubset = ""
        haystack = ""

        for i in range(1, len(letters) + 1):  # from 1 to avoid empty subsets
            subset = letters[0:i]
            haystack = self.rows[position:]
            index = haystack.find(subset)

            if index != -1:
                maxIndex = index
                maxSubset = subset
                continue

        return maxSubset, maxIndex

    def appendLetters(self, letters):
        for letter in letters:
            self.appendLetter(letter)

    def appendLetter(self, letter):
        for index, c in enumerate(self.rows):
            if c == "_":
                self.rows = self.rows[0:index] + letter + self.rows[index+1:]
                return index
        raise NoLayoutError("No more space for " + letter)

    def __str__(self):
        return self.formatRows(self.rows)

    def size(self):
        index = self.rows.find("_")
        if index == -1:
            return self.numRows * (self.rowSize+1) # Max if not found
        return index

    def formatRows(self, rows):
        s = ""
        for i in range(self.numRows):
            for j in range(self.rowSize):
                s += rows[i*(self.rowSize +1) + j]
            s += "\n"
        return s

    def illuminateWord(self, word):
        return self.illuminateIndexes(self.getIndexesForWord(word))

    def illuminateIndexes(self, indexes):
        illuminated = ""
        position = 0
        for index in indexes:
            illuminated += "." * (index - position) + self.rows[index]
            position = index + 1
        illuminated += "." * (len(self.rows) - position) 
        return self.formatRows(illuminated)

    def getWordsAndIndexes(self, words): # [['Words]]
        return [[word, self.getIndexesForWord(word)] for word in words]

    def getIndexesForWord(self, word):
        indexes = []
        position = 0
        for letter in word:
            index = self.rows.find(letter, position)
            indexes.append(index)
            position = index + 1
        return indexes

    def indexesToLedNumber(self, indexes):
        return [index - index // (self.rowSize + 1) for index in indexes] #removing one EOL character each line 

    def getWordsAndLedNumbers(self, words):
        wordsAndIndexes = self.getWordsAndIndexes(words)
        return  [[i[0], self.indexesToLedNumber(i[1])] for i in wordsAndIndexes ]

        #realIndex = index - (index // (self.rowSize + 1)) # remove EOL separators to have a LED number

        


def createLayout(words):
    layout = Layout(config.height, config.width)
    for word in words:
        layout.addLettersIfNeeded(word)
    return layout

