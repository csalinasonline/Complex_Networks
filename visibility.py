"""Visibility Graph Script

This script allows the user to run a vsibility graph on data

This tool accepts comma separated value files (.csv).

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
    series = np.random.normal(loc=6, scale=0.1, size=(N,1))
    # binomial
    #series = np.random.binomial(n=10, p=0.7, size=(N,1))
    # Poisson
    #series = np.random.poisson(lam=2, size=(N,1))
    # Uniform
    #series = np.random.uniform(size=(N, 1))
    # Logistic
    #series = np.random.logistic(loc=1, scale=2, size=(N, 1))
    # Multi
    #series = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
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
    
    G = nx.Graph()
    g = visibility_graph(series)
    print(g.nodes())
    print(g.edges())
    x = list(g.nodes())
    y = series
    e = list(g.edges())
    plt.stem(x,y)
    plt.figure(1)
    for edg in e:
        plt.plot(edg, [y[(edg[0])], y[(edg[1])]])
    
    plt.figure(2)
    nx.draw(g)
    plt.figure(3)
    plt.hist(y)
if __name__ == "__main__":
    main()
    
