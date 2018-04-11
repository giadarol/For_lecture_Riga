import numpy as np
from math import sin, cos

def generate_particles(N_part):
    x = np.random.randn(N_part)
    xp = np.random.randn(N_part)
    return x, xp

#@profile
def rotate_particles(x, xp):

    N_part = len(x)

    for ii in range(N_part):
        
        theta = np.pi/3. + 0.01*x[ii]
        costh = cos(theta)
        sinth = sin(theta)
        
        x_new = x[ii]*costh + xp[ii]*sinth
        xp_new = -xp[ii]*sinth + x[ii]*costh

        x[ii] = x_new
        xp[ii] = xp_new


def rotate_particles_vect(x, xp):
    
    theta = np.pi/3. + 0.01*x
    costh = np.cos(theta)
    sinth = np.sin(theta)
    
    x_new = x*costh + xp*sinth
    xp_new = -xp*sinth + x*costh

    x[:] = x_new
    xp[:] = xp_new
    
    
import rotate_cython as rc


#@profile
def doit():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rotate_particles(x, xp)

def doit_vect():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rotate_particles_vect(x, xp)
    
def doit_cython():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rc.rotate_particles(x, xp)

doit()

import timeit
exectime = timeit.timeit(stmt = 'doit()',  setup = 'from __main__ import doit', number=2)
print('Exec. time: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_vect()',  setup = 'from __main__ import doit_vect', number=2)
print('Exec. time vect: %.2f s'%exectime)

import timeit
exectime = timeit.timeit(stmt = 'doit_cython()',  setup = 'from __main__ import doit_cython', number=2)
print('Exec. time vect: %.2f s'%exectime)

# to profile:
# kernprof --view -l 000_profile_example.py



