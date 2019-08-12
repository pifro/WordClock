from __future__ import print_function
from layout import Layout
from itertools import permutations

words = [
    "JULIE",  "MARTHE", "MARIE-DO", "PIERRE", "MARIE",
    "THERESE", "MICHELE", "CHRISTINE", "MADELEINE"]


def createLayout(words):
    layout = Layout(10, 11)
    for word in words:
        layout.addLettersIfNeeded(word)
    return layout


def dumbBruteForceOptimizer(words):

    bruteForce = list(permutations(words))
    count = len(bruteForce)

    minSize = 100
    finalLayout = ""
    finalPermutation = ""

    for i, permutation in enumerate(bruteForce):
        layout = createLayout(permutation)
        size = layout.size()
        if size < minSize:
            minSize = size
            finalLayout = layout
            print("*", end="")
        if i % 10000 == 0:
          print(str(i) + "/" + str(count) + ":" + str(size) + "/" + str(minSize))

    return finalLayout, finalPermutation


layout = createLayout(words)
print(layout)
