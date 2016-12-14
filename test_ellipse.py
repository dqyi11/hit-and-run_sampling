'''
Created on Dec 14, 2016

@author: daqingy
'''

import numpy as np
from constrained_sampling import *
import matplotlib.pyplot as plt
from shapely import geometry

def ellipse_polyline(x0, y0, a, b, angle, n=100):
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    st = np.sin(t)
    ct = np.cos(t)

    angle = np.deg2rad(angle)
    sa = np.sin(angle)
    ca = np.cos(angle)
    p = np.empty((n, 2))
    p[:, 0] = x0 + a * ca * ct - b * sa * st
    p[:, 1] = y0 + a * sa * ct + b * ca * st
    
    result = geometry.Polygon(p)
    return result


if __name__ == '__main__':
    
    elli = ellipse_polyline(1, 1, 2, 1, 45)
    poly_x, poly_y = elli.exterior.xy
    
    N = 500
    init_pos = np.array([0.4,0.6])
    X = hit_and_run_sampling( N, elli, init_pos )
    plt.scatter(X[:,0],X[:,1])
    plt.plot(np.hstack([poly_x,poly_x[0]]), np.hstack([poly_y,poly_y[0]]),'b')
    plt.show()
    
    
