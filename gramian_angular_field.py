"""Gramian Angular Field Plots Script

This script allows the user to run a recurrence plots on data

This script requires requirements.txt.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField
from collections import deque

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
    
    # rotate data and aggregate
    X = list()
    s_list = list(series)
    d_list = deque(s_list)
    i = 0
    for _ in range(len(series)):
        d_list.rotate(i)
        X.append(list(d_list))
        i = i + 1
    
    # Recurrence plot transformation
    X_num = np.squeeze(np.array(X))
    transformer = GramianAngularField()
    X_new = transformer.transform(X_num)      
    
    plt.figure(1)
    plt.plot(series)
    plt.show()
    
    plt.figure(2)
    for idx, _ in enumerate(series):
        plt.clf()
        plt.subplot(211)
        plt.imshow(X_new[idx], cmap='binary', origin='lower')
        plt.title('GramianAngularField Plot ' + str(idx), fontsize=16)
        plt.tight_layout()    
        plt.subplot(212)
        plt.plot(series)
        plt.scatter(idx,series[idx])
        plt.tight_layout()  
        plt.show()
        time.sleep(0.1)
    
    plt.figure(3)
    plt.hist(series)
    plt.show()
#    
if __name__ == "__main__":
    main()
    
