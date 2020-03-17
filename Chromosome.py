'''
Created on 17 mar. 2020

@author: George
'''


from random import randint, seed
from utils import generateARandomPermutation
import numpy as np


# permutation-based representation
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam  #problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0.0
    
    
    @property
    def repres(self):
        return self.__repres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c): #inmultire de permutari (algebra)
        # algebraic permutation operations XO (improvement: converges faster to result)
        np_self_repres = np.array(self.__repres)
        np_c_repres = np.array(c.__repres)
        np_offspring = np_c_repres[np_self_repres] # numpy builtin overloaded operator for permutation multiplication
        new_repres = np_offspring.tolist()
        
        offspring = Chromosome(self.__problParam)
        offspring.repres = new_repres
        return offspring

    
    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        
    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

