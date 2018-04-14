#convert -coalesce Z_cutoff_sigma1000_monitor_1cm_giovanni_Ey.gif f%04d.png
import matplotlib.pyplot as plt
import matplotlib.patches as mp



fname = 'photograms_illustration/f0005.png'
img = plt.imread(fname)

y = 187.5
x = 277.
L = 120

figsize = (8, 8.*img.shape[0]/img.shape[1])


plt.close('all')

fig1 = plt.figure(1, figsize=figsize)
ax = plt.subplot(1,1,1)
# ax.axis('off')
ax.imshow(img)
# plt.plot([x-L/2, x+L/2], [y, y], '-r', linewidth=5)
ax.add_patch(mp.Ellipse((x,y), height=10, width=L, alpha=.8, color='r'))
ax.axis('tight')

fig1.savefig(fname.split('.png')[0]+'_modif.png', dpi=90, bbox_inches='tight')

# fig1.subplots_adjust(bottom=0, top=1., left=0., right=1.)

plt.show()
