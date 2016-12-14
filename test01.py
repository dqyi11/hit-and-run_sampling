'''
Created on Dec 13, 2016

@author: daqingy
'''

if __name__ == '__main__':
    
    
    from shapely import geometry
    import numpy as np
    from constrained_sampling import *
    
    poly = geometry.Polygon([[0,0],[2,0],[2,2],[0,2]])
    rnd_val = generate_random_direction()
    line = geometry.LineString([(0.5,0.5),(0.5 + rnd_val[0] * 10, 0.5 + rnd_val[1] * 10)])
    
    intersecs = poly.intersection(line)
    
    sec_x, sec_y = intersecs.coords.xy
    tmin = np.array([sec_x[0], sec_y[0]])
    tmax = np.array([sec_x[len(sec_x)-1], sec_y[len(sec_y)-1]])
    y = tmin + (tmax-tmin) * np.random.rand()
    
    print y