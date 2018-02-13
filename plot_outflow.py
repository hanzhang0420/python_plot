import aplpy
from pylab import *
from scipy.io.idl import readsav
import matplotlib.pyplot as plt
from scipy import ndimage
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
import aplpy   # a python package that can impose images 
from pylab import *
from scipy.io.idl import readsav
import matplotlib.pyplot as plt
from scipy import ndimage
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from matplotlib import rc, font_manager
import matplotlib.colors as colors
import numpy as np
from viridis import viridis

mpl.rcParams['font.family'] = 'sans-serif'

#w51irs2cc=aplpy.FITSFigure('W51_IRS2_20140617-CANARICAM-Imaging_rot-20.fits')
#w51irs2cc.show_colorscale(vmin=0.005, vmax=0.12, cmap=viridis,pmax=99)
#w51irs2c=aplpy.FITSFigure('w51_te_continuum_best.fits')
#w51irs2c.show_colorscale(vmin=0.0002, vmax=0.01, cmap=Blues,pmax=98)

#levs=np.zeros(7)
#sigma=0.005
#for i in range(7):
#    levs[i]=sigma*(0.04/(sigma))**(i*1.0/7.0)
#w51irs2cc.show_contour('CBand_ACarray_continuum.fits',levels=levs,colors='w',linewidths=1.5)

#sigma=0.005
#for i in range(7):
#    levs[i]=sigma*(0.06/(sigma))**(i*1.0/7.0)

#w51irs2cc.show_contour('KuBand_BDarray_continuum.fits',levels=levs,colors='m',linewidths=1.5)

#sigma=0.008
#for i in range(6):
#    levs[i]=sigma*(0.04/(sigma))**(i*1.0/6.0)

#w51irs2cc.show_contour('w51_te_continuum_best.fits',levels=levs,colors='g')
#text(8.5,.55,'8.6 $\mu$m',fontsize=11)

#w51irs2cc.save('myplot.eps')
fig = plt.figure()
w51irs2cc=aplpy.FITSFigure('W51_IRS2_20140617-CANARICAM-Imaging_rot-20.fits')
w51irs2cc.show_colorscale(vmin=0.005, vmax=0.12, cmap=cm.jet,pmax=98)

lev_r=np.zeros(5)
lev_b=np.zeros(5)
sigma=0.25
for i in range(5):
    lev_r[i]=5*sigma*(9.7960837/(5*sigma))**(i*1.0/6.0)
    lev_b[i]=5*sigma*(6.7749335/(5*sigma))**(i*1.0/6.0)

#levs=np.zeros(6)
#for i in range(6):
#    levs[i]=sigma*(0.04/(sigma))**(i*1.0/7.0)
sig2=0.015
levs=np.linspace(1,6,6)*sig2

w51irs2cc.show_contour('w51_12co2-1_blue0to45.fits',levels=lev_b,colors='skyblue',linewidths=1.0,label='CO2-1 blue0-45')
w51irs2cc.show_contour('w51_12co2-1_red73to130.fits',levels=lev_r,colors='coral',linewidths=1.0,label='CO2-1 red73-130')
w51irs2cc.show_contour('integrated_Ha_60-16_rot20.fits',levels=levs,colors='purple',linewidths=1.5,label='H77$\alpha$')

plt.plot(2,3,'skyblue',label='CO2-1 blue0-45')
plt.plot(2,3,'coral',label='CO2-1 red73-130')
plt.plot(2,3,'purple',label='H77$\\alpha$')

#select four points in the map to show the decomposition steps 


legend = plt.legend(loc='lower left',prop={'size': 9})
plt.annotate('d1',xy=(62,57),xycoords='data',xytext=(49,70),arrowprops=dict(facecolor='white',shrink=0.01,width=0.02,headwidth=0.0,color='w'),color='w',size=14)
plt.annotate('OKYM2',xy=(59,38),xycoords='data',xytext=(30,20),arrowprops=dict(facecolor='white',shrink=0.01,width=0.02,headwidth=0.0,color='w'),color='w',size=14)
plt.annotate('IRS 2E',xy=(72,32),xycoords='data',xytext=(75,12),arrowprops=dict(facecolor='white',shrink=0.01,width=0.02,headwidth=0.0,color='w'),color='w',size=14)
plt.annotate('IRS 2W',xy=(115,58),xycoords='data',xytext=(127,82),arrowprops=dict(facecolor='white',shrink=0.01,width=0.02,headwidth=0.0,color='w'),color='w',size=14)
plt.annotate('Lacy Jet',xy=(94,46),xycoords='data',xytext=(104,20),arrowprops=dict(facecolor='white',shrink=0.01,width=0.02,headwidth=0.0,color='w'),color='w',size=14)

w51irs2cc.save('myplot_outflow.eps')
