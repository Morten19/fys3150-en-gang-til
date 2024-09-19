


import numpy as np


a=([2,-1,0,0,0])
b=([-1,2,-1,0,0])
c=([0,-1,2,-1,0])
e=([0,0,-1,2,-1])
f=([0,0,0,-1,2])

h=([1,1.6,1.8,1.6,1])

g=np.array([a,b,c,e,f])



def funk(x,y):
    return (np.dot(x,y))


print(funk(g,h))

#python3 test.py
#[0.4 0.4 0.4 0.4 0.4]






















