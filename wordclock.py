
from __future__ import print_function
from layout import Layout
from itertools import permutations
from random import randint
from pprint import pprint

words = [
    "JULIE",  "MARTHE", "MARIE-DO", "PIERRE", "MARIE",
    "THERESE", "MICHELE", "CHRISTINE", "MALO", "ALBANE",
    "GREGOIRE", "AUGUSTIN", "BRIEUC", "ELOI", "INES", "LOUIS",
    "LAURE", "JEAN-MARIE", "BERTRAND"]

WIDTH = 11
HEIGHT = 10

def createLayout(words):
    layout = Layout(HEIGHT, WIDTH)
    for word in words:
        layout.addLettersIfNeeded(word)
    return layout


def dumbBruteForceOptimizer(words):

    if len(words) > 10:
        raise Exception('Too Many Words for n!')

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



def swapWords(words):
    size = len(words)
    a = randint(0, size - 1)
    b = randint(0, size - 1)
    swapped = words.copy()
    swapped[a] = words[b]
    swapped[b] = words[a]
    return swapped
    

def initPopulation(words, popSize): # a member is a tuple (words, score)
    population = []
    score = evaluateWords(words)
    for i in range(popSize):
        population.append([words, score])
    return population

def mutatePopulation(population, protectSize):
    populationToMutate = population[protectSize:]
    mutatedPopulation = list(map(mutateMember, populationToMutate))
    return population[0:protectSize] + mutatedPopulation

def mutateMember(member):
    newWords = swapWords(member[0])
    return [newWords, evaluateWords(newWords)]

def evaluateWords(words):
    layout = createLayout(words)
    return layout.size()

def cullPopulation(population, selectSize):        
    population = sorted(population, key=lambda x: x[1])
    return population[0:selectSize] 

def reproducePopulation(population, popSize):
    factor = int(popSize / len(population))
    newPopulation = population * factor
    return newPopulation

def populationScores(population):
    return [i[1] for i in population ]


def geneticOptimizer(words, numGen, popSize=100, selectSize=5):
    population = initPopulation(words, popSize)
    bestWords = []
    for i in range(numGen):
        print("*** GEN " + str(i) + " ***")
        #pprint(population)
        #print("M")

        population = mutatePopulation(population, selectSize)
        #pprint(population)
        population = cullPopulation(population, selectSize)

        population = reproducePopulation(population, popSize)

        #print("R")
        #pprint(population)
        #print(population[0])
        #print(populationScores(population)[0])
        bestWords = sorted(population, key=lambda x: x[1])[0][0]
        print(createLayout(bestWords))
    return bestWords


        

if __name__ == "__main__":

    words = geneticOptimizer(words, 100, 1000, 100)
    print(words)
    print(createLayout(words))


