import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot

# p=probability, kelly=the betting amount

def coinflip(p,kelly):
    flips=-np.ones([1,100])
    for i in xrange(int(round(p))):
        flips[[0][0]][i]=1
    return flips[0]*kelly

# n=number of paths, t=time intervals

def simulation(n,t,data):
    a=np.array([])
    b=np.array([])
    for i in range(n):
        a=np.column_stack(np.random.choice(data,size=t,replace=True))
        b=np.append(a,b)
    b=b.reshape(t,n)
    mc = pd.DataFrame(b, index=np.arange(0,t,1), columns=np.arange(0,n,1))
    mc=1+mc
    mc=mc.cumprod()
    data_median=[]
    data_mean=[]
    for i in xrange(t):
        data_median.append(np.median(mc.values[i]))
        data_mean.append(mc.values[i].mean())
    plt.plot( np.array(data_median), 'r-',  np.array(data_mean), 'k')
    plt.legend(['Median Final Value' +str(np.array(data_median[-1:])), 'Average Final Value' +str(np.array(data_mean[-1:]))])
    plt.ylabel('Value')
    plt.xlabel('Iterations')
    plt.title('Mean and Median Evolution with Kelly Over-Betting')
    plt.show()
    plt.figure(1)
    plt.subplot(211)
    plt.xlabel('Iterations')
    plt.ylabel('Gains')
    plt.title('Monte Carlo Simulation | Average Final Value ' + str(round(mc.values[-1].mean(),2))+ ' | Standard Deviation ' + str(round(mc.values[-1].std(),2))+ ' | Return/Risk Ratio ' + str(round(((mc.values[-1].mean())-1)/mc.values[-1].std(),2)))
    plt.plot(mc, label='$y = {i}x + {i}$'.format(i=i), linewidth=1, alpha=0.5)
    plt.subplot(212)
    plt.xlabel('Gains after Iterations')
    plt.ylabel('Frequency')
    plt.hist(mc.values[-1], bins=100, facecolor='#636363', alpha=0.75, linewidth=.2, edgecolor='black')
    plt.axvline(mc.values[-1].mean(), color='k', linestyle='dashed', linewidth=1)
    plt.axvline(np.median(mc.values[-1]), color='blue', linestyle='dashed', linewidth=1)
    plt.legend(['Average value of '  + str(round(mc.values[-1].mean(),2)), 'Median value of '+  str(round(np.median(mc.values[-1]),2)) ])
    pyplot.show()

coin_data=coinflip(51,0.02)

simulation(1000,500,coin_data)
