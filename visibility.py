"""Visibility Graph Script

This script allows the user to run a vsibility graph on data

This script requires requirements.txt.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from visibility_graph import visibility_graph

N = 100
start = 0
end = 2*math.pi
spacing = (end-start)/N
samples = np.arange(start, end, spacing)

def sin_f(x): 
    return math.sin(np.float(x))

def cos_f(x): 
    return math.cos(np.float(x))

def tan_f(x): 
    return math.tan(np.float(x))

def main():
    # sine
    #sin = np.vectorize(sin_f) 
    #series = sin(samples)

    # cos
    #cos = np.vectorize(cos_f) 
    #series = cos(samples)
    
    # tan
    #tan = np.vectorize(tan_f) 
    #series = tan(samples)    
    
    # normal
    #series = np.random.normal(loc=6, scale=0.1, size=(N,1))
    # binomial
    #series = np.random.binomial(n=10, p=0.7, size=(N,1))
    # Poisson
    #series = np.random.poisson(lam=2, size=(N,1))
    # Uniform
    #series = np.random.uniform(size=(N, 1))
    # Logistic
    #series = np.random.logistic(loc=1, scale=2, size=(N, 1))
    # Multi
    series = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    # Exponential
    #series = np.random.exponential(scale=2, size=(N, 1))
    # Chi
    #series = np.random.chisquare(df=2, size=(N, 1))
    # Rayleigh
    #series = np.random.rayleigh(scale=2, size=(N, 1))
    # Pareto
    #series = np.random.pareto(a=2, size=(N, 1))  
    # Zipf
    #series = np.random.zipf(a=2, size=(N, 1))
    
    g = visibility_graph(series)
    # Circular
    #pos = nx.circular_layout(g)
    # Bipartite
    #top = nx.bipartite.sets(g)[0]
    #pos = nx.bipartite_layout(g, top)   
    # Kamada Kawai
    #pos = nx.kamada_kawai_layout(g)
    # Planar
    #pos = nx.planar_layout(g)
    # Random
    #pos = nx.random_layout(g) 
    # Shell
    shells = [[0], list(np.arange(1, len(g), 1))]
    pos = nx.shell_layout(g, shells)
    # Spring
    #pos = nx.spring_layout(g) 
    # Spectral
    #pos = nx.spectral_layout(g)    
    # Spiral
    #pos = nx.spiral_layout(g)
    # Multipartite
    #pos = nx.multipartite_layout(g)
        
    
    print(g.nodes())
    print(g.edges())
    x = list(g.nodes())
    y = series
    e = list(g.edges())
    plt.stem(x,y)
    plt.figure(1)
    for edg in e:
        plt.plot(edg, [y[(edg[0])], y[(edg[1])]])
    plt.show()
    
    plt.figure(2)
    nx.draw(g,pos)
    #nx.draw_networkx_labels(g,pos,font_size=7,font_family='sans-serif')
    #nx.draw_networkx_edge_labels(g,pos,q_list,label_pos=0.3)
    plt.show()
    
    plt.figure(3)
    plt.hist(y)
    plt.show()
    
if __name__ == "__main__":
    main()
    
