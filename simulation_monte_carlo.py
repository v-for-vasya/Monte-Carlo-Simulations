
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=[0.1,0.1,0.1,0.1,0.1,0.1,-0.1,-0.1,-0.1,-0.1]

def monte_carlo(n,t,data): #n=number of paths, t=time intervals
    b=np.array([])
    for i in range(n):
        a=np.column_stack(np.random.choice(data,size=t,replace=True))
        b=np.append(a,b)
    b=b.reshape(t,n)
    mc = pd.DataFrame(b, index=np.arange(0,t,1), columns=np.arange(0,n,1))
    mc=mc.cumsum()
    print mc[:-1][-1:]
    mc.plot(legend =False, color=['0.1', '0.12', '0.14','0.16','0.18','0.2', '0.22', '0.25', '0.3', '0.35', '0.4', '0.45', '0.5'])
    print 'median value ' + str(np.median(mc[:-1][-1:]))
    plt.title('Monte Carlo Simulation')
    plt.show()

monte_carlo(1000,500,data)
