


import numpy as np

import matplotlib.pyplot as plt
def f(x):
    return 1-(1-np.exp(-10))*x-np.exp(-10*x)


q=np.array([1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,10/10])
list1=f(q)

bb=list1 #lengde 10

plt.plot(q,f(q))
#plt.xlabel("x")
#plt.ylabel("u(x)")
#plt.show()



a = -1
b=2
c=-1


nn=10
A = np.linspace(0,0,nn)
B = np.linspace(0,0,nn)
C = np.linspace(0,0,nn)
D = np.linspace(0,0,nn)

E=np.array([A]*10)


np.fill_diagonal(E, [2, 2, 2])

for i in range(9):
    E[i][i+1]=-1


for j in range(9+1):
    E[j][j-1]=-1


Einv=np.linalg.inv(E)

qq=(np.dot(Einv,bb))

plt.plot(q,qq)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("n=10, orange = exact solution, blue = matrix approximation")
plt.show()

print(qq)















