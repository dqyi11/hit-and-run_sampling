'''
Created on Dec 12, 2016

@author: daqingy
'''

import numpy as np
from shapely import geometry


                 
def generate_random_direction():
    p = np.random.randn(2)
    return p/np.linalg.norm(p)


def get_random_sample_toward_intersection(x, rnd_dir, poly, R):
    x1 = x
    x2 = x + rnd_dir * R
    line = geometry.LineString([(x1[0],x1[1]),(x2[0], x2[1])])
    
    intersecs = line.intersection(poly)
    sec_x, sec_y = intersecs.coords.xy
    tmin = np.array([sec_x[0], sec_y[0]])
    tmax = np.array([sec_x[len(sec_x)-1], sec_y[len(sec_y)-1]])
    y = tmin + (tmax-tmin) * np.random.rand()
    return y
    

def hit_and_run_sampling(sampling_num, poly, init_pos, discard_num=200):
    
    X = np.zeros((sampling_num+discard_num, 2))
    n = 0
    
    (minx, miny, maxx, maxy) = poly.bounds
    R = np.sqrt((maxx-minx)**2 + (maxy-miny)**2)
    
    while n < sampling_num + discard_num:
        # generate a Direction
        rnd_dir = generate_random_direction()
        
        
        rnd_pos = get_random_sample_toward_intersection(init_pos, rnd_dir, poly, R)
        
        if poly.contains( geometry.Point([rnd_pos[0], rnd_pos[1]]) ):
            X[n,:] = rnd_pos
        else:
            X[n,:] = init_pos

        init_pos = X[n,:]
        n += 1
        print n
        
    return X[discard_num:,:]
    
    
    
    