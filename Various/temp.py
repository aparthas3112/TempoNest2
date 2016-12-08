chains=np.loadtxt('./TwoCompScatterHessChain/chain_1.txt').T
burnin=10000
ML=chains.T[np.argmax(chains[-3][burnin:])][:n_params]

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import LogNorm
from matplotlib.ticker import MultipleLocator

def WaterFallPlot(lfunc, ML):

lfunc.doplot = True
Res, Data, Model =lfunc.FFTMarginLogLike(ML)

Res=np.array(Res).T
Data=np.array(Data).T	
Model=np.array(Model).T

x=np.float64(lfunc.psr.stoas)
tdiff = np.max(lfunc.psr.stoas) - np.min(lfunc.psr.stoas)
aspectgoal = 16.0/6
aspect=tdiff/aspectgoal

fig, (ax1, ax2) = plt.subplots(2,1)

im1 = ax1.imshow(np.log10(np.abs(Data)), interpolation="none", extent=(x[0], x[-1], 0, 1), aspect=aspect)
#divider1 = make_axes_locatable(ax1)
# Append axes to the right of ax3, with 20% width of ax3
#cax1 = divider1.append_axes("right", size="20%", pad=0.05)
# Create colorbar in the appended axes
# Tick locations can be set with the kwarg `ticks`
# and the format of the ticklabels with kwarg `format`
#cbar1 = plt.colorbar(im1, cax=cax1, ticks=MultipleLocator(0.2), format="%.2f")

im2 = ax2.imshow(np.abs(Res), interpolation="none", extent=(np.min(x), np.max(x), 0, 1), aspect=aspect)
#divider2 = make_axes_locatable(ax2)
# Append axes to the right of ax3, with 20% width of ax3
#cax2 = divider2.append_axes("right", size="20%", pad=0.05)
# Create colorbar in the appended axes
# Tick locations can be set with the kwarg `ticks`
# and the format of the ticklabels with kwarg `format`
#cbar2 = plt.colorbar(im2, cax=cax2, ticks=MultipleLocator(0.2), format="%.2f")

plt.show()

WaterFallPlot(ML)
