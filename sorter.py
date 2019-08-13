from __future__ import print_function
from itertools import permutations
from random import randint
from pprint import pprint

import config
import layout

def dumbBruteForceOptimizer(words):

    if len(words) > 10:
        raise RuntimeError('Too Many Words  ( n! is painful )')

    bruteForce = list(permutations(words))
    count = len(bruteForce)

    minSize = 100
    finalGrid = ""
    finalPermutation = ""

    for i, permutation in enumerate(bruteForce):
        grid = grid.createLayout(permutation)
        size = grid.size()
        if size < minSize:
            minSize = size
            finalGrid = grid
            print("*", end="")
        if i % 10000 == 0:
          print(str(i) + "/" + str(count) + ":" + str(size) + "/" + str(minSize))

    return finalGrid, finalPermutation



def swapWords(words):
    size = len(words)
    a = randint(0, size - 1)
    b = randint(0, size - 1)
    swapped = list(words)
    swapped[a] = words[b]
    swapped[b] = words[a]
    return swapped
    

def initPopulation(words, popSize): # a member is a lisr [words, score]
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
    try:
        grid = layout.createLayout(words)
        return grid.size()
    except layout.NoLayoutError:
        return config.height * (config.width + 1) #Max possible

def cullPopulation(population, selectSize):        
    population = sorted(population, key=lambda x: x[1])
    return population[0:selectSize] 

def reproducePopulation(population, popSize):
    factor = int(popSize / len(population))
    newPopulation = population * factor
    return newPopulation

def populationScores(population):
    return [i[1] for i in population ]


def geneticSorter(words, numGen, popSize=100, selectSize=5):
    population = initPopulation(words, popSize)
    bestMember = []
    for i in range(numGen):
        print("*** GEN " + str(i) + " ***")

        population = mutatePopulation(population, selectSize)
        population = cullPopulation(population, selectSize)
        population = reproducePopulation(population, popSize)
        bestMember = sorted(population, key=lambda x: x[1])[0]

        print(bestMember[1])
        try:
            print(layout.createLayout(bestMember[0]))
        except layout.NoLayoutError:
            print("No Layout Found")
        
    return bestMember[0]


    