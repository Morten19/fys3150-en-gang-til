


import numpy as np

a=([2,-1,0,0,0,0,0,0,0,0])
b=([-1,2,-1,0,0,0,0,0,0,0])
c=([0,-1,2,-1,0,0,0,0,0,0])
e=([0,0,-1,2,-1,0,0,0,0,0])
f=([0,0,0,-1,2,-1,0,0,0,0])
g=([0,0,0,0,-1,2,-1,0,0,0])
h=([0,0,0,0,0,-1,2,-1,0,0])
i=([0,0,0,0,0,0,-1,2,-1,0])
j=([0,0,0,0,0,0,0,-1,2,-1])
k=([0,0,0,0,0,0,0,0,-1,2])



A=np.array([a,b,c,e,f,g,h,i,j,k])


def funk(x,y):
    return (np.dot(x,y))

b= np.array([0.532,0.664,0.650,0.5817,0.493,0.397,0.299,0.1997,0.099,0])

Ainv = np.linalg.inv(A)



sol=(funk(Ainv,b))

x=np.array([1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,10/10])

sol2=np.array([sol,x])

np.savetxt("data_7.txt",sol2, fmt='%.2e')












