import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c as clight
import time

sigmaz = 30.

R_ring = 100.

n_part = 1000

Qx = 6.18

Amplx = 5

z_part = np.linspace(-sigmaz, sigmaz, n_part)
x_part = 0.*z_part

theta_ring = np.linspace(0, 2*np.pi, 1000)
X_ring = R_ring*np.cos(theta_ring)
Y_ring = R_ring*np.sin(theta_ring)

L_ring = 2*np.pi*R_ring
T_rev = L_ring/clight

N_turns = 30
N_frames = 500

t_vect = np.linspace(0, N_turns*T_rev, N_frames)
i_turn_vect = np.arange(0, (N_turns+2), 1.)

fname = 'damped'
Amplx_vect_turn = 10 * np.exp(-i_turn_vect/10) 


Amplx_vect_turn = 1 * np.exp(i_turn_vect/10) 

plt.close('all')
plt.figure(1, figsize=(8*1.7,6))
plt.ion()
sp1 = plt.subplot(1,2,1)
sp2 = plt.subplot(1,2,2)

for ii, tt in enumerate(t_vect):

	print ii

	s_part = z_part + clight*tt
	thata_part = s_part/R_ring

	Amplx_part = np.interp(s_part/L_ring, i_turn_vect, Amplx_vect_turn)

	phix_part = 2*np.pi*s_part/L_ring*Qx
	x_part = Amplx_part*np.cos(phix_part)

	X_part = (R_ring+x_part)*np.cos(thata_part)
	Y_part = (R_ring+x_part)*np.sin(thata_part)

	sp1.clear()

	sp1.plot(X_ring, Y_ring)
	sp1.axis('equal')

	sp1.set_xlim(-R_ring*1.1, R_ring*1.1)
	sp1.set_ylim(-R_ring*1.1, R_ring*1.1)
	sp1.set_aspect('equal',adjustable='box')

	sp1.plot(X_part, Y_part, '.r')

	i_turn = np.floor(np.mean(s_part)/L_ring)
	x_turn = Amplx_vect_turn[i_turn]*np.cos(2*np.pi*i_turn/(Qx%1))

	sp1.set_title('Frame %d Turn %.1f'%(ii, i_turn))
	sp2.plot(i_turn, Amplx_vect_turn[i_turn], 'bo')
	sp2.set_xlim(0, N_turns)

	plt.savefig('tmpout/a%04d.png'%ii, dpi=100)

	# plt.pause(0.01)
	# plt.draw()



# plt.show()