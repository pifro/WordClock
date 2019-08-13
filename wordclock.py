
from __future__ import print_function
from pprint import pprint

import config
import layout
import sorter

if __name__ == "__main__":
    
    words = config.words
    
    #words = sorter.geneticSorter(words, numGen=25, popSize=200, selectSize=20)
    print(words)    
    grid = layout.createLayout(words)
    for word in words:
        print(grid.illuminateWord(word))
        print(grid.illuminateIndexes(grid.getIndexesForWord(word)))

    print(grid)
    pprint(grid.getWordsAndLedNumbers(words))
    print(str(len(words)) + " words packed")

