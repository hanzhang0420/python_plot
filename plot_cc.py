import matplotlib.pyplot as plt
from numpy import *
from pylab import *
from matplotlib.ticker import MultipleLocator
from matplotlib import rc, font_manager
from scipy.io.idl import readsav
import pyfits
from matplotlib.ticker import MultipleLocator
from matplotlib import rc, font_manager
from matplotlib.colors import LogNorm
#mpl.rcParams['font.size'] = 12.
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['axes.labelsize'] = 14.
mpl.rcParams['xtick.labelsize'] = 11.
mpl.rcParams['ytick.labelsize'] = 11.

I_8_7=readsav('/scratch/hanzhang/GTC_data/result/object/wl_16/combine/I_8_7.sav').I_8_7*((1.0/0.08)**2)
I_10_3=readsav('/scratch/hanzhang/GTC_data/result/object/wl_16/combine/I_10_3.sav').I_10_3*((1.0/0.08)**2)
I_12_5=readsav('/scratch/hanzhang/GTC_data/result/object/wl_16/combine/I_12_5.sav').I_12_5*((1.0/0.08)**2)

plt.figure()
ax1=subplot(311)
n=I_10_3.shape
x=np.linspace(0,n[1]-1,n[1])
y=np.linspace(0,n[0]-1,n[0])
sigma=0.03
#levels=np.linspace(15,600,18)*sigma
lev=np.zeros(8)
for i in range(8):
#    print i
    lev[i]=7*sigma*(I_8_7.max()/(7*sigma))**(i*1.0/9.0)
print lev

im=plt.imshow(I_8_7,interpolation='bilinear', origin='lower',cmap=cm.gray_r,extent=(0,0,0,0))
csf=plt.pcolormesh(I_8_7,cmap=cm.hot,vmin=0.2, vmax=5.0)
cs=plt.contour(I_8_7,lev,colors='w',linewidth=0.1)

#spiral_arm_x=[31.2,32,35,39]
#spiral_arm_y=[20,19,16.5,15]
#plt.plot(spiral_arm_x,spiral_arm_y,'b--',linewidth=3.0)
#spiral_arm_x=[52,54,54.5,54.8,53.7]
#spiral_arm_y=[15,12,11,7.49,6.2]
#plt.plot(spiral_arm_x,spiral_arm_y,'b--',linewidth=3.0)

u_a=0.05*np.cos(120*np.pi/180)*60
v_a=0.05*np.sin(120*np.pi/180)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5,label='N')
qk = quiverkey(Q,abs(0.05*n[1]),abs(0.75*n[0]) ,np.nan ,'N', labelpos='N',labelcolor='w',coordinates='data')
u_a=0.05*np.cos(120*np.pi/180+np.pi/2)*60
v_a=0.05*np.sin(120*np.pi/180+np.pi/2)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5)
qk = quiverkey(Q,abs(0.00*n[1]),abs(0.550*n[0]) ,np.nan ,'E', labelpos='E',labelcolor='w',coordinates='data')
plt.setp(ax1.get_yticklabels(), visible=False)
plt.setp(ax1.get_xticklabels(), visible=False)

#text(60,5,'S shape',fontsize=11,color='w')

ax2=subplot(312)

xx,yy=np.meshgrid(x,y)
im=plt.imshow(I_10_3,interpolation='bilinear', origin='lower',cmap=cm.gray_r,extent=(0,0,0,0))
csf=plt.pcolormesh(xx,yy,I_10_3,cmap=cm.hot)

sigma=0.0178658
lev=np.zeros(8)
for i in range(8):
    lev[i]=7*sigma*(I_10_3.max()/(7*sigma))**(i*1.0/8.0)
print lev


level=np.linspace(6,300,25)*0.02
csf=plt.contour(I_10_3,lev,colors='w',linewidth=0.1)
#cbar=plt.colorbar(csf,shrink=1.0,orientation='Vertical')
#cbar.ax.set_xlabel('Surface Brightness (Jy arcsec$^{-2}$)',fontsize=10)


#plt.xlabel("Pixels")
u_a=0.05*np.cos(120*np.pi/180)*60
v_a=0.05*np.sin(120*np.pi/180)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5,label='N')
qk = quiverkey(Q,abs(0.05*n[1]),abs(0.75*n[0]) ,np.nan ,'N', labelpos='N',labelcolor='w',coordinates='data')
u_a=0.05*np.cos(120*np.pi/180+np.pi/2)*60
v_a=0.05*np.sin(120*np.pi/180+np.pi/2)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5)
qk = quiverkey(Q,abs(0.00*n[1]),abs(0.550*n[0]) ,np.nan ,'E', labelpos='E',labelcolor='w',coordinates='data')

#plt.title('10.3 $\mu$m')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)

u_a=0.06*np.cos(120*np.pi/180)*60
v_a=0.06*np.sin(120*np.pi/180)*60
Q=quiver(69,9,u_a,v_a,width=0.006,headwidth=0,headlength=0,headaxislength=0,color='w',scale_units='xy', scale=0.5,label='N')

text(70,5,'Dark Lane',fontsize=11,color='w')

ax3=subplot(313)
#I_12_5=readsav('/scratch/hanzhang/GTC_data/result/object/wl_16/combine/I_12_5.sav').I_12_5*((1.0/0.08)**2) #in unit of mJy 

n=I_12_5.shape
print n
im=plt.imshow(I_12_5,interpolation='bilinear', origin='lower',cmap=cm.gray_r,extent=(0,0,0,0))
csf=plt.pcolormesh(I_12_5,cmap=cm.hot)

sigma=0.06
lev=np.zeros(7)
for i in range(7):
    lev[i]=7*sigma*(I_12_5.max()/(7*sigma))**(i*1.0/6.0)
print lev


level=np.linspace(6,200,25)*0.05
csf=plt.contour(I_12_5,lev,colors='w',linewidth=0.1)
#csf=plt.contour(I_12_5,80,cmap=cm.gnuplot2)
#cbar=plt.colorbar(csf,shrink=1.0,orientation='Vertical')
#cbar.ax.set_xlabel('Surface Brightness (Jy arcsec$^{-2}$)',fontsize=10)
u_a=0.05*np.cos(120*np.pi/180)*60
v_a=0.05*np.sin(120*np.pi/180)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5,label='N')
qk = quiverkey(Q,abs(0.05*n[1]),abs(0.75*n[0]) ,np.nan ,'N', labelpos='N',labelcolor='w',coordinates='data')
u_a=0.05*np.cos(120*np.pi/180+np.pi/2)*60
v_a=0.05*np.sin(120*np.pi/180+np.pi/2)*60
Q=quiver(abs(0.1*n[1]),abs(0.67*n[0]),u_a,v_a,width=0.006,color='w',scale_units='xy', scale=0.5)
qk = quiverkey(Q,abs(0.00*n[1]),abs(0.550*n[0]) ,np.nan ,'E', labelpos='E',labelcolor='w',coordinates='data')

loc_x=[72,82.5]
loc_y=[4,4]
plt.plot(loc_x,loc_y,'w',linewidth=3.0,label='1.0 arcsec')
text(70,5,'1.0 arcsec',fontsize=11,color='w')

#plt.title('12.5 $\mu$m')


#plt.title('Q2 Image')
plt.setp(ax3.get_yticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)


subplots_adjust(wspace=0.05,hspace=0.1)

#ax4.yaxis.set_label_position('right')
#ax4.yaxis.set_ticks_position('right')
#legend = plt.legend(loc='center left',prop={'size': 9})
plt.savefig('/scratch/hanzhang/GTC_data/result/object/wl_16/VLT_data/wl_16_other.eps',bbox_inches='tight')
#
plt.show()
