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

figsize = (8*1.2,6)


fig1 = plt.figure(1)
fig1.set_facecolor('w')
ax1 = plt.subplot(1,1,1)
ax1.plot(chamb.Vx*1e3, chamb.Vy*1e3, '-', linewidth=3)
ax1.plot(x_mp*1e3, y_mp*1e3, '.g', markersize=2)
ax1.axis('equal')

fig2 = plt.figure(2, figsize=figsize)
fig2.set_facecolor('w')
ax2 = plt.subplot(1,1,1)
cbinfo = ax2.pcolormesh(pic.xg*1e3, pic.yg*1e3, pic.rho.T)
cb = plt.colorbar(cbinfo)
cb.formatter.set_powerlimits((0, 0))
cb.update_ticks()
cb.set_label('Charge density [C/m^3]')
ax2.plot(chamb.Vx*1e3, chamb.Vy*1e3, '-y', linewidth=3)
ax2.axis('equal')


fig3 = plt.figure(3, figsize=figsize)
fig3.set_facecolor('w')
ax3 = plt.subplot(1,1,1)
cbinfo=ax3.pcolormesh(pic.xg*1e3, pic.yg*1e3, pic.phi.T)
cb = plt.colorbar(cbinfo)
cb.formatter.set_powerlimits((0, 0))
cb.update_ticks()
cb.set_label('Electic potential [V]')
ax3.plot(chamb.Vx*1e3, chamb.Vy*1e3, '-y', linewidth=3)
ax3.axis('equal')

fig4 = plt.figure(4, figsize=figsize)
fig4.set_facecolor('w')
ax4 = plt.subplot(1,1,1)
cbinfo=ax4.pcolormesh(pic.xg*1e3, pic.yg*1e3, pic.efx.T)
cb = plt.colorbar(cbinfo)
cb.formatter.set_powerlimits((0, 0))
cb.update_ticks()
cb.set_label('Ex [V/m]')
ax4.plot(chamb.Vx*1e3, chamb.Vy*1e3, '-y', linewidth=3)
ax4.axis('equal')


fig5 = plt.figure(5, figsize=figsize)
fig5.set_facecolor('w')
ax5 = plt.subplot(1,1,1)
cbinfo=ax5.pcolormesh(pic.xg*1e3, pic.yg*1e3, np.sqrt(pic.efx**2 + pic.efy**2).T)
cb = plt.colorbar(cbinfo)
cb.formatter.set_powerlimits((0, 0))
cb.update_ticks()
cb.set_label('Electric field magnitude [V/m]')
ax5.plot(chamb.Vx*1e3, chamb.Vy*1e3, '-y', linewidth=3)
ax5.axis('equal')

for ifig, fig, ax in zip(range(5), [fig1, fig2, fig3, fig4, fig5], [ax1, ax2, ax3, ax4, ax5]):
	ax.set_xlabel('x [mm]')
	ax.set_ylabel('y [mm]')
	fig.subplots_adjust(bottom=.12)
	fig.savefig('figure_%d.png'%ifig, dpi=200)


plt.show()