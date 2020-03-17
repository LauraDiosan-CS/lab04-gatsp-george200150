'''
Created on 17 mar. 2020

@author: George
'''

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import warnings


def plotAFunction(xref, yref, x, y, xoptimal, yoptimal, message):    
    plt.plot(xref, yref, 'b-')
    plt.plot(x, y, 'ro', xoptimal, yoptimal, 'bo')
    plt.title(message)
    plt.show()
    plt.pause(0.9)
    plt.clf()

# plot the network 
def plotRawNetwork(net):
    warnings.simplefilter('ignore')
    
    A=np.matrix(net) # network["mat"]
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(7, 7)) 
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show(G)
    

def plotCommunities(path, network):
    A=np.matrix(network["mat"])
    G=nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(7, 7))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size = 600, cmap = plt.cm.RdYlBu, node_color = path)
    nx.draw_networkx_edges(G, pos, alpha = 0.3)
    plt.show(G)
    plt.pause(0.9)
    plt.clf()


