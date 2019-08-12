from __future__ import print_function


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
                raise Exception(
                    'Recursion! :' + letters + '/' + remainingLetters)

            if len(remainingLetters) > 0:
                self.addLettersIfNeeded(remainingLetters, position + index)

    def findBiggestSubsetAndIndex(self, letters, position):
        maxIndex = -1
        maxSubset = ""
        haystack = ""

        for i in range(1, len(letters) + 1):  # from 1 to avoid empty subsets
            subset = letters[0:i]
            haystack = self.rows[position:]
            index = haystack.find(subset)
            #  print("Looking for " + subset + " in " + haystack)
            if index != -1:
                maxIndex = index
                maxSubset = subset
                continue

        #  if maxIndex != -1:
        #  print(maxSubset + " found at " + str(maxIndex) + " in " + haystack)

        return maxSubset, maxIndex

    def appendLetters(self, letters):
        for letter in letters:
            self.appendLetter(letter)

    def appendLetter(self, letter):
        for index, c in enumerate(self.rows):
            if c == "_":
                self.rows = self.rows[0:index] + letter + self.rows[index+1:]
                return index
        raise Exception("No more space for " + letter)

    def __str__(self):
        s = ""
        for c in self.rows:
            if c == "|":
                s += "\n"
            else:
                s += c
        return s

    def size(self):
        return self.rows.find("_")

    def illuminate(self, word):
        return ""
