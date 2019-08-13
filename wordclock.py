
from __future__ import print_function
from pprint import pprint

import config
import layout
import sorter

if __name__ == "__main__":
    
    words = config.words
    
    words = sorter.geneticSorter(words, numGen=25, popSize=1000, selectSize=10)
    print(words)    
    grid = layout.createLayout(words)
    for word in words:
        print(grid.illuminateWord(word))
        print(grid.illuminateIndexes(grid.getIndexesForWord(word)))


    print("*** LAYOUT ***")
    print("")
    print(grid)
    print('*** WORDS AND LED NUMBER ***')
    print("")
    pprint(grid.getWordsAndLedNumbers(words))
    print(str(len(words)) + " words packed")

