from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# x= capital, p=probability of success, g=payoff, l=loss/cost, t=time interval
def simulate(x,p,g,l,t):
    x=[x]
    for i in xrange(t):
        outcome=int(np.random.choice([1,-1],1,p=[p,1-p,]))
        if (x[i] <= l):
            x.append(0)
        else:
            if outcome==abs(outcome):
                x.append(x[i] + outcome*g)
            else:
                x.append(x[i] + outcome*l)
    return x

n=600
array=np.column_stack(simulate(100,0.01,1000,1,300) for i in xrange(n))

print 'average final value ' + str(sum(array[-1])/len(array[-1]))
print 'median value ' + str(np.median(array[-1]))
print 'mode value ' + str(stats.mode(array[-1])[0])
print 'number of bankruptcies: ' + str(np.count_nonzero(array[-1] == 0))
print 'probability of being bankrupt at the end: ' + str(round(np.count_nonzero(array[-1] == 0)/n*100,2)) + '%'

avg=[]
median=[]
for i in xrange(len(array)):
    avg.append(sum(array[i])/len(array[i]))
    median.append(np.median(array[i]))

plt.plot(array, color=[0.15,0.2,0.3,0.35])
plt.plot(avg, color='r')
plt.plot(median, color='#52a0d8')
plt.ylabel('Gains')
plt.xlabel('Time')
plt.legend(['Average final value ' + str(round(sum(array[-1])/len(array[-1]),2))])
plt.title('Monte Carlo Simulation ')
plt.show()

