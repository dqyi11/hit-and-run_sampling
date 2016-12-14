'''
Created on Dec 13, 2016

@author: daqingy
'''

if __name__ == '__main__':
    
    
    from shapely import geometry
    import numpy as np
    from constrained_sampling import *
    
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
    
    
        
    elli = ellipse_polyline(1, 1, 2, 1, 45)
    poly_x, poly_y = elli.exterior.xy
    
    rnd_val = generate_random_direction()
    line = geometry.LineString([(0.5,0.5),(0.5 + rnd_val[0] * 10, 0.5 + rnd_val[1] * 10)])
    
    intersecs = line.intersection(elli)
    
    sec_x, sec_y = intersecs.coords.xy
    tmin = np.array([sec_x[0], sec_y[0]])
    tmax = np.array([sec_x[len(sec_x)-1], sec_y[len(sec_y)-1]])
    y = tmin + (tmax-tmin) * np.random.rand()
    
    print y