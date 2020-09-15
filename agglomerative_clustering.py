"""Agglomerative Clustering Plots Script

This script allows the user to run a Agglomerative Clustering plots on data

This script requires requirements.txt.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img 
from dtaidistance import dtw
from dtaidistance import clustering
import dtaidistance.dtw_visualisation as dtwvis

def main():
    s = np.array([
         np.flip([0., 0, 1, 2, 1, 0, 1, 0, 0, 1]),
         [0., 1, 2, 0, 0, 0, 0, 0, 0, 1],
         np.flip([1., 2, 0, 0, 0, 0, 0, 1, 1, 1],0),
         [0., 0, 1, 2, 1, 0, 1, 0, 0, 1],
         [0., 1, 2, 0, 0, 0, 0, 0, 0, 1],
         np.flip([1., 2, 0, 0, 0, 0, 0, 1, 1, 1],0),
         np.flip([1., 2, 0, 0, 0, 0, 0, 1, 1, 1],0)])
    
    # Custom Hierarchical clustering
    model1 = clustering.Hierarchical(dtw.distance_matrix_fast, {})
    cluster_idx = model1.fit(s)
    # Keep track of full tree by using the HierarchicalTree wrapper class
    model2 = clustering.HierarchicalTree(model1)
    cluster_idx = model2.fit(s)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
    show_ts_label = lambda idx: "ts-" + str(idx)
    model2.plot('hierarchy.jpg', axes=ax, show_ts_label=show_ts_label,
               show_tr_label=True, ts_label_margin=-10,
               ts_left_margin=10, ts_sample_length=1)
    
    # reading png image file 
    im = img.imread('hierarchy.jpg') 

    # show image
    plt.imshow(im)
    
if __name__ == "__main__":
    main()