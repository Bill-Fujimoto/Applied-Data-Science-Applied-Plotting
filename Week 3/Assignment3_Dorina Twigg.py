#%matplotlib notebook
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_palette( 'RdBu_r')
import matplotlib.pyplot as plt
import scipy.stats as st
np.random.seed(12345)
import math
from matplotlib import cm
df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df = df.T
bplt = sns.boxplot( data=df,whis='range',palette=['w','w','w','w'])

def onclick(event):
    mynum =event.ydata
    plt.cla()
    plt.gca().set_title('Y = {}'.format( int(round(mynum)) ) )
    
    probs = []
    for c in df.columns:
        prob = st.norm.cdf((mynum - df[c].mean())/df[c].std())
        probs.append( prob )
    colors=plt.cm.RdBu(  probs  )
    bplt = sns.boxplot( data=df,whis='range',palette=colors)
    plt.axhline( mynum,color='k' )
    

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event',onclick)
