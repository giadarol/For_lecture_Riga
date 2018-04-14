#convert -coalesce Z_cutoff_sigma1000_monitor_1cm_giovanni_Ey.gif f%04d.png


import matplotlib.pyplot as plt

fname = 'f0000.png'
img = plt.imread(fname)

figsize = (8, 8.*img.shape[0]/img.shape[1])


plt.close('all')

fig1 = plt.figure(1, figsize=figsize)
ax = plt.subplot(1,1,1)
# ax.axis('off')
ax.imshow(img)
plt.plot([400], [200], 'o')
ax.axis('tight')

fig1.savefig(fname.split('.png')[0]+'_modif.png', dpi=90, bbox_inches='tight')

# fig1.subplots_adjust(bottom=0, top=1., left=0., right=1.)

plt.show()
