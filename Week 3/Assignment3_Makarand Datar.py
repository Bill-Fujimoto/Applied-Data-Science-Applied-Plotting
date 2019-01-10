# Option 2 implementation
# Use the following data for this assignment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#import seaborn as sbn

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])

summary = df.T.describe().T
summary['95% bound on mean'] = 1.96*summary['std']/(summary['count']**0.5)
index = np.arange(4)
#fig, ax = plt.subplots()
fig = plt.figure()
ax = plt.gca()

def choosecolor(row,b):
    if ((row['mean']-row['95% bound on mean'])>b):
        return 'firebrick'
    elif ((row['mean']+row['95% bound on mean'])<b):
        return 'steelblue'
    else:
        return 'white'

def finddistancetomean(row,b):
    return row['mean']-b

def choosecolorscale(distanceSeries):
    #print(distanceSeries)
    colorgradeperdist = max(abs(distanceSeries))/128
    colorscale = np.floor(128+(distanceSeries/colorgradeperdist))
    colorscale = colorscale.astype(int)
    return colorscale

def choosecolor(scale):
    return plt.get_cmap('seismic')(scale)

def colorbar(uservalue):
    distance = summary.apply(lambda x:finddistancetomean(x,uservalue),axis=1)
    colorscale = choosecolorscale(distance)
    colorchoice = colorscale.apply(choosecolor)
    #print(colorchoice)
    bar_width = 0.95
    plt.bar(index, summary['mean'].values, bar_width,yerr=summary['95% bound on mean'],capsize=10,color=colorchoice,edgecolor='black')
    ax.set_xticks(index+bar_width/8)
    ax.set_xticklabels(summary.index,fontsize=12)
    ax.set_title('Mean Quantity vs Year',fontsize=14)
    plt.show()
    #plt.colorbar()

colorbar(39000)
