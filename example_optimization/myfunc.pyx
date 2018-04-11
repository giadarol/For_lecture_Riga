
from math import sin, cos, pi

def rotate_particles(x, xp):

	N_part = len(x)

	for ii in range(N_part):
		
		theta = pi/3. + 0.01*x[ii]
		costh = cos(theta)
		sinth = sin(theta)
		
		x_new = x[ii]*costh + xp[ii]*sinth
		xp_new = -xp[ii]*sinth + x[ii]*costh

		x[ii] = x_new
		xp[ii] = xp_new
