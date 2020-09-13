"""Dynamic Time Warping Plots Script

This script allows the user to run a Dynamic Time Warping  plots on data

This script requires requirements.txt.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""
import numpy as np
import matplotlib.pyplot as plt
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

def main():
    s1 = np.array([0., 0, 1, 2, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0])
    s2 = np.array([0., 1, 2, 3, 1, 0, 0, 0, 2, 1, 0, 0, 0])
    path = dtw.warping_path(s1, s2)
    dtwvis.plot_warping(s1, s2, path)
    
    plt.figure(1)
    plt.subplot(211)
    plt.title('Timeseries: s1 & s2')
    plt.plot(s1)
    plt.subplot(212)
    plt.plot(s2)
    plt.show()
    
    dist = dtw.distance(s1, s2)
    print(dist)
    
    plt.figure(2)
    d, paths = dtw.warping_paths(s1, s2, window=3, psi=2)
    best_path = dtw.best_path(paths)
    dtwvis.plot_warpingpaths(s1, s2, paths, best_path)
    
if __name__ == "__main__":
    main()