import numpy as np
from math import sin, cos
import numba


def generate_particles(N_part):
    x = np.random.randn(N_part)
    xp = np.random.randn(N_part)
    return x, xp


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

@numba.autojit
def rotate_numba(x, xp):

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
    
    
import myfunc as rc
import rotate_fortran as rf


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
    
def doit_cython_opt():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rc.rotate_particles_opt(x, xp)

def doit_fortran():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rf.rotate_fortran(x, xp)

def doit_numba():
    N_part = 1000000
    x, xp = generate_particles(N_part)
    rotate_numba(x, xp)

doit()


import timeit
exectime = timeit.timeit(stmt = 'doit()',  setup = 'from __main__ import doit', number=2)
print('Exec. time: %.2f s'%exectime)

exectime = timeit.timeit(stmt = 'doit_vect()',  setup = 'from __main__ import doit_vect', number=2)
print('Exec. time vect: %.2f s'%exectime)

import timeit
exectime = timeit.timeit(stmt = 'doit_cython()',  setup = 'from __main__ import doit_cython', number=2)
print('Exec. time cython: %.2f s'%exectime)

import timeit
exectime = timeit.timeit(stmt = 'doit_cython_opt()',  setup = 'from __main__ import doit_cython_opt', number=2)
print('Exec. time cython opt: %.2f s'%exectime)

import timeit
exectime = timeit.timeit(stmt = 'doit_fortran()',  setup = 'from __main__ import doit_fortran', number=2)
print('Exec. fortran: %.2f s'%exectime)

import timeit
exectime = timeit.timeit(stmt = 'doit_numba()',  setup = 'from __main__ import doit_numba', number=2)
print('Exec. numba: %.2f s'%exectime)

# to profile:
# kernprof --view -l 000_profile_example.py



