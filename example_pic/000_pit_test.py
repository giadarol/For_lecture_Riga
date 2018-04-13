import sys
sys.path.append('../../PyFRIENDS')

import matplotlib.pyplot as plt
import numpy as np

randn = np.random.randn

import PyECLOUD.geom_impact_poly_fast_impact as gip
import PyECLOUD.mystyle as ms
import PyPIC.FiniteDifferences_ShortleyWeller_SquareGrid as PIC_FDSW


chamb = gip.polyg_cham_geom_object(filename_chm='LHC_chm_ver.mat', flag_non_unif_sey=False)

pic = PIC_FDSW.FiniteDifferences_ShortleyWeller_SquareGrid(chamb = chamb, Dh = 0.2e-3)


N_first_cluster = 5000
x_mp = randn(N_first_cluster)*3e-3 + 8e-3
y_mp = randn(N_first_cluster)*2e-3 + 5e-3

N_second_cluster = 5000
x_mp = np.concatenate((x_mp, randn(N_first_cluster)*2e-3 - 8e-3))
y_mp = np.concatenate((y_mp, randn(N_first_cluster)*3e-3 - 5e-3))
n_mp = -(x_mp*0+2e11/len(x_mp)/10e-2)

pic.scatter(x_mp, y_mp, nel_mp=n_mp)
pic.solve()

plt.close('all')
ms.mystyle_arial(fontsz=16)


fig1 = plt.figure(1)
fig1.set_facecolor('w')
ax1 = plt.subplot(1,1,1)
ax1.plot(chamb.Vx, chamb.Vy, '-', linewidth=3)
ax1.plot(x_mp, y_mp, '.g', markersize=2)
ax1.axis('equal')

fig2 = plt.figure(2)
fig2.set_facecolor('w')
ax2 = plt.subplot(1,1,1)
ax2.pcolormesh(pic.xg, pic.yg, pic.rho.T)
ax2.plot(chamb.Vx, chamb.Vy, '-y', linewidth=3)
ax2.axis('equal')

fig3 = plt.figure(3)
fig3.set_facecolor('w')
ax3 = plt.subplot(1,1,1)
ax3.pcolormesh(pic.xg, pic.yg, pic.phi.T)
ax3.plot(chamb.Vx, chamb.Vy, '-y', linewidth=3)
ax3.axis('equal')

fig4 = plt.figure(4)
fig4.set_facecolor('w')
ax4 = plt.subplot(1,1,1)
ax4.pcolormesh(pic.xg, pic.yg, pic.efx.T)
ax4.plot(chamb.Vx, chamb.Vy, '-y', linewidth=3)
ax4.axis('equal')


fig5 = plt.figure(5)
fig5.set_facecolor('w')
ax5 = plt.subplot(1,1,1)
ax5.pcolormesh(pic.xg, pic.yg, np.sqrt(pic.efx**2 + pic.efy**2).T)
ax5.plot(chamb.Vx, chamb.Vy, '-y', linewidth=3)
ax5.axis('equal')



plt.show()