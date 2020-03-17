'''
Created on 17 mar. 2020

@author: George
'''

from Chromosome import Chromosome
from utils_plotting import plotRawNetwork
from random import seed
from GA import GA
from utils_plotting import plotCommunities
from utils import __readNet
import utils_plotting


import matplotlib.pyplot as plt


#fitness function for TSP
def detCost(cyc, param):
    graph = param['mat']
    cost = 0
    
    for i in range(0, len(cyc)-1):
        src = cyc[i]
        dst = cyc[i+1]
        edgeCost = graph[src][dst]
        cost += edgeCost
        
    
    cost += graph[cyc[i+1]][cyc[0]] # so that the path becomes cyclic

    return cost



if __name__ == '__main__':
    #network = __readNet('tsp.txt')
    network = __readNet('hard.txt')
    #network = __readNet('medium.txt')
    #network = __readNet('easy.txt')
    plotRawNetwork(network['mat'])
    
    
    MIN = -1
    MAX = 1
    N = network['noNodes'] 
    fcEval = detCost
    
    
    seed(1)
    
    gaParam = {'popSize' : 100, 'noGen' : 250, 'pc' : 0.8, 'pm' : 0.1}
    problParam = {'min' : MIN, 'max' : MAX, 'function' : fcEval, 'noDim' : 1, 'noNodes' : N, 'network': network}
    
    # store the best/average solution of each iteration (for a final plot used to anlyse the GA's convergence)
    allBestFitnesses = []
    allAvgFitnesses = []
    generations = []
    
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    
    bestRepres = None
    
    for g in range(gaParam['noGen']):
        #plotting preparation
        allPotentialSolutionsX = [c.repres for c in ga.population]
        allPotentialSolutionsY = [c.fitness for c in ga.population]
        bestSolX = ga.bestChromosome().repres
        bestSolY = ga.bestChromosome().fitness
        
        if bestRepres == None or bestSolY < detCost(bestRepres, network): # PROBLEM OF GLOBAL MINIMA
            bestRepres = bestSolX
        
        allBestFitnesses.append(bestSolY)
        allAvgFitnesses.append(sum(allPotentialSolutionsY) / len(allPotentialSolutionsY))
        generations.append(g)
    
        #logic alg
        #ga.oneGeneration()
        ga.oneGenerationElitism()
        #ga.oneGenerationSteadyState()
        
        
        
        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
    
    

    # https://github.com/lauradiosan/AI-2019-2020/blob/master/lab04/lab04.pdf
    communities = bestRepres
    print("BEST OVERALL ",communities)
    plotCommunities(communities, network)
    cost = detCost(communities, network)
    print(cost)
    
    # GRAFIC DE CONVERGENTA
    plt.ioff()
    best, = plt.plot(generations, allBestFitnesses, 'ro', label = 'best')
    mean, = plt.plot(generations, allAvgFitnesses, 'bo', label = 'mean')
    plt.legend([best, (best, mean)], ['Best', 'Mean'])
    plt.show()
    
    #cost = detCost([0, 1, 2, 6, 3, 7, 5, 4], network)
    #print("MINIMA = ",cost)
