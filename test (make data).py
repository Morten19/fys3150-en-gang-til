



import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,1,100)



def funk(t):
    return 1-(1-np.exp(-10))*t-np.exp(-10*t)

x=(funk(t))


plt.plot(t,x)

c=(np.array([t,x]))


d=c.T

np.savetxt("data.txt",d, fmt='%.2e')

e=np.loadtxt("data.txt")

print(e[:,0])






