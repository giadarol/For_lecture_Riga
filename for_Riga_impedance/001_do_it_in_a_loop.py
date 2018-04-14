#convert -coalesce Z_cutoff_sigma1000_monitor_1cm_giovanni_Ey.gif f%04d.png
import matplotlib.pyplot as plt
import matplotlib.patches as mp

frame_ref_1 = 5
x_ref_1 = 277.

frame_ref_2 = 8
x_ref_2 = 490.

y = 187.5
L = 120

flag_witness = False
witness_delay = 2.5*400.

for i_frame in range(0, 50):
	fname = 'photograms_illustration/f%04d.png'%i_frame
	img = plt.imread(fname)
	
	x = x_ref_1+(i_frame-frame_ref_1)*(x_ref_2-x_ref_1)/(frame_ref_2-frame_ref_1)

	x_witness = x - witness_delay


	figsize = (8, 8.*img.shape[0]/img.shape[1])


	plt.close('all')

	fig1 = plt.figure(1, figsize=figsize)
	ax = plt.subplot(1,1,1)
	ax.axis('off')
	ax.imshow(img)
	# plt.plot([x-L/2, x+L/2], [y, y], '-r', linewidth=5)
	ax.add_patch(mp.Ellipse((x,y), height=10, width=L, alpha=.8, color='r'))
	if flag_witness:
		ax.add_patch(mp.Ellipse((x_witness,y), height=10, width=L, alpha=.8))
	ax.axis('tight')
	ax.set_xlim(left=0., right=800.)

	fig1.subplots_adjust(bottom=0, top=1., left=0., right=1.)
	fig1.savefig(fname.split('.png')[0]+'_modif.png', dpi=90, bbox_inches='tight')

 

plt.show()

import os
os.system('ffmpeg -i photograms_illustration/f%04d_modif.png -c:v libx264 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2,setpts=3.0*PTS"  -profile:v high -level:v 4.0 -pix_fmt yuv420p -crf 22 -codec:a aac Output.mp4')


