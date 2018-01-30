# Function plot_pol_map is used to plot polarization maps 
# Input: the scale factor; IDL structure file contains polarization percentage, polarization position angles, intensity, polarizatin intensity etc; the direction of the North; sigma errors; the name of the output plot
# Package: numpyl matplot readsav 
 
from pylab import *
import numpy as np
from scipy.io.idl import readsav
import matplotlib.pyplot as plt
from scipy import ndimage
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from matplotlib import rc, font_manager
import matplotlib.colors as colors

def plot_pol_map(f,file,pwd,n_dir,sigma,name):
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['axes.labelsize'] = 14.
    mpl.rcParams['xtick.labelsize'] = 11.
    mpl.rcParams['ytick.labelsize'] = 11.

#readin idl sav data
    p=readsav(file).p
    t=readsav(file).t
    I=readsav(file).I#*((1.0/0.08)**2)  #in unit of mJy square arcsec^2 
    ip=readsav(file).ip#;*((1.0/0.08)**2) 

#####################################################################################
    n=p.shape
    print n

    x=np.linspace(0,n[1]-1,n[1])
    y=np.linspace(0,n[0]-1,n[0])
    xx,yy=np.meshgrid(x,y)
#linear contour levels
    levels=np.linspace(1,30,10)*I.max()/30
#exponential contour levels
    lev=np.zeros(7)
    for i in range(7):
        lev[i]=5*sigma*(I.max()/(5*sigma))**(i*1.0/7.0)

    im=plt.imshow(I,interpolation='bilinear', origin='lower',cmap=cm.gray_r,extent=(0,0,0,0))
    csf=plt.pcolormesh(xx,yy,I,cmap=cm.Blues,norm=colors.PowerNorm(gamma=1.0/2.0))
    cs=plt.contour(I,lev,linewidths=.6,colors='b')
#####################################################################################
#make a log scaled leves
    lev_ip=np.zeros(9)
    for j in range(9):
        lev_ip[j]=3*1.41*sigma*(ip.max()/(3*1.41*sigma))**(j*1.0/9.0)
    
#    cbar=plt.colorbar(csf,shrink=0.8,orientation='vertical')
#    cbar.ax.set_ylabel('Polarized Intensity ip (Jy arcsec$^{-2}$)',fontsize=10)
#    cbar.ax.set_ylabel('Intensity I (Jy arcsec$^{-2}$)',fontsize=10)
#plot vectors, plot twice in order to make the vector center at the (x,y) point

###################################make sure plot at the center pixel#####################################
    color_v='k' #set the color of the vectors  

    u_a=0.5*p*np.cos(t)*f
    v_a=0.5*p*np.sin(t)*f
    u_a=ma.masked_array(u_a,mask=abs(u_a[:,:]) > 1.2)
    v_a=ma.masked_array(v_a,mask=abs(v_a[:,:]) > 1.2)
    Q_a=quiver(xx,yy,u_a,v_a,width=0.008,headwidth=0,headlength=0,headaxislength=0,color=color_v,scale_units='xy', scale=0.2)

    u_a=0.5*p*np.cos(t+np.pi)*f
    v_a=0.5*p*np.sin(t+np.pi)*f
    u_a=ma.masked_array(u_a,mask=abs(u_a[:,:]) > 1.2)
    v_a=ma.masked_array(v_a,mask=abs(v_a[:,:]) > 1.2)
    Q_a=quiver(xx,yy,u_a,v_a,width=0.008,headwidth=0,headlength=0,headaxislength=0,color=color_v,scale_units='xy', scale=0.2)

##################################plot scale##################################################################
    color_s='g'
    u_a=0.05*np.cos(0*np.pi/180)*f
    v_a=0.05*np.sin(0*np.pi/180)*f
    Q=quiver(abs(0.85*n[1]),abs(0.86*n[0]),u_a,v_a,width=0.002,headwidth=0,headlength=0,headaxislength=0,color=color_s,scale_units='xy', scale=0.2,label='5%')
    qk = quiverkey(Q, abs(0.87*n[1]),abs(0.84*n[0]),np.nan ,'5%', labelpos='N',labelcolor=color_s,coordinates='data')

#######################################plot ticks#######################################################################
    ax=plt.gca()

    x1=np.linspace(0,n[1]-1,5)
    y1=np.linspace(0,n[0]-1,5)

    xticks=(-np.linspace(0,n[1]-1,5)+(n[1]-1)/2.0)*0.08
    yticks=(np.linspace(0,n[0]-1,5)-(n[0]-1)/2.0)*0.08
    plt.xticks(x1,xticks)
    plt.yticks(y1,yticks)
    plt.ylabel("$\delta_{arcsec}$")
    plt.xlabel("$\delta_{arcsec}$")

###########################################plot_N_direction###################################################
    color_n='k'
    u_a=0.06*np.cos((90+n_dir)*np.pi/180)*30
    v_a=0.06*np.sin((90+n_dir)*np.pi/180)*30
    Q=quiver(abs(0.14*n[1]),abs(0.85*n[0]),u_a,v_a,width=0.006,color=color_n,scale_units='xy', scale=0.5,label='N')
    u_a=0.06*np.cos((180+n_dir)*np.pi/180)*30
    v_a=0.06*np.sin((180+n_dir)*np.pi/180)*30
    Q=quiver(abs(0.14*n[1]),abs(0.85*n[0]),u_a,v_a,width=0.002,color=color_n,scale_units='xy', scale=0.5)
 #  plt.title('Polarization map'+name)
    plt.savefig(pwd+'Plot'+name+'.eps')
    plt.show()

