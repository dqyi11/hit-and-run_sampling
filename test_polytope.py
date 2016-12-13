'''
Created on Dec 12, 2016

@author: daqingy
'''

from constrained_sampling import *
import numpy as np 
import matplotlib.pyplot as plt
from shapely import geometry

if __name__ == '__main__':
    
    V = [[0.18, 0.49], [0.02, 0.01], [0.46, 0.49], [0.72, 0.94], [0.42, 0.85]]
    
    N = 500
    init_pos = np.array([0.4,0.6])
    poly = geometry.Polygon(V)   
    poly_x, poly_y = poly.exterior.xy

        
    X = hit_and_run_sampling( N, poly, init_pos )
    plt.scatter(X[:,0],X[:,1])
    plt.plot(np.hstack([poly_x,poly_x[0]]), np.hstack([poly_y,poly_y[0]]),'b')
    plt.show()
    