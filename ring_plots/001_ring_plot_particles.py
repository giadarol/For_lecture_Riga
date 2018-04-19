import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import c as clight
import time

import mystyle as ms

sigmaz = 15.

R_ring = 100.

n_part = 200

Qx = 6.18

Amplx = 5

# z_part = np.linspace(-sigmaz, sigmaz, n_part)
z_part = np.random.randn(n_part)*sigmaz
A_part_inco = np.random.randn(n_part)*3
phi0_part_inco = np.random.rand(n_part)*2*np.pi

theta_ring = np.linspace(0, 2*np.pi, 1000)
X_ring = R_ring*np.cos(theta_ring)
Y_ring = R_ring*np.sin(theta_ring)

L_ring = 2*np.pi*R_ring
T_rev = L_ring/clight

N_turns = 18
N_frames = 450

t_vect = np.linspace(0, N_turns*T_rev, N_frames)
i_turn_vect = np.arange(0, (N_turns+2), 1.)


fname = 'stationary'
Amplx_vect_turn = 0 * np.exp(-i_turn_vect/10)

# fname = 'damped'
# Amplx_vect_turn = 7 * np.exp(-i_turn_vect/10) 

fname = 'instab'
Amplx_vect_turn = 1 * np.exp(i_turn_vect/7.) 

plt.close('all')
ms.mystyle_arial(fontsz=16)
fig1 = plt.figure(1, figsize=(8*1.7,6))
fig1.set_facecolor('w')
plt.ion()
sp1 = plt.subplot(1,2,1)
sp2 = plt.subplot(1,2,2)
sp2.set_xlabel('Turn')
sp2.set_ylabel('Oscillation amplitude')


for ii, tt in enumerate(t_vect):

	print ii

	s_part = z_part + clight*tt
	thata_part = s_part/R_ring

	Amplx_part = np.interp(s_part/L_ring, i_turn_vect, Amplx_vect_turn)

	phix_part = 2*np.pi*s_part/L_ring*Qx
	x_part = Amplx_part*np.cos(phix_part) + A_part_inco*np.cos(phix_part+phi0_part_inco)

	X_part = (R_ring+x_part)*np.cos(thata_part)
	Y_part = (R_ring+x_part)*np.sin(thata_part)

	sp1.clear()

	sp1.plot(X_ring, Y_ring, linewidth=3)
	sp1.axis('equal')
	sp1.axis('off')

	sp1.set_xlim(-R_ring*1.1, R_ring*1.1)
	sp1.set_ylim(-R_ring*1.1, R_ring*1.1)
	sp1.set_aspect('equal',adjustable='box')

	sp1.plot(X_part, Y_part, '.r')

	i_turn = int(np.floor(np.mean(s_part)/L_ring))
	if i_turn==-1:i_turn=0
	x_turn = Amplx_vect_turn[i_turn]*np.cos(2*np.pi*i_turn/(Qx%1))

	sp1.set_title('Turn %.0f'%(i_turn))
	sp2.plot(i_turn, Amplx_vect_turn[i_turn], '.b', markersize=14)
	sp2.set_xlim(0, N_turns)
	sp2.grid('on')
	sp2.set_ylim(bottom=0., top=np.max(Amplx_vect_turn)*1.1)

	plt.subplots_adjust(left=0,right=.95, wspace=.1)
	plt.savefig('tmpout/part_%s_a%04d.png'%(fname, ii), dpi=90)


	# plt.pause(0.01)
	# plt.draw()r
import os
os.system(' '.join([
    'ffmpeg',
    '-i tmpout/part_%s'%(fname)+'_a%04d.png',
    '-c:v libx264 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2,setpts=1.*PTS"',
    '-profile:v high -level:v 4.0 -pix_fmt yuv420p -crf 22 -codec:a aac part_%s.mp4'%fname]))


# plt.show()