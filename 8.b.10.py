


import numpy as np

import matplotlib.pyplot as plt

#superdiagonal -1, 2, -1
#superdiagonal a,b,c

#length 10, 100, 1000



#C=np.tile(10,A)
#print(B)

#Av=g

#så b er verdiene til u(x) i de 10 punktene

def f(x):
    return 1-(1-np.exp(-10))*x-np.exp(-10*x)

#x=1/10 u(x) = 0.532


q=np.array([1/10,2/10,3/10,4/10,5/10,6/10,7/10,8/10,9/10,10/10])
list1=f(q)

bb=list1 #lengde 10

plt.plot(q,f(q))
#plt.xlabel("x")
#plt.ylabel("u(x)")
#plt.show()


#Aa = b


a = -1
b=2
c=-1


nn=10
A = np.linspace(0,0,nn)
B = np.linspace(0,0,nn)
C = np.linspace(0,0,nn)
D = np.linspace(0,0,nn)

#A=np.array([a,a,0,0])
#B=np.array([a,b,b,0])
#C=np.array([0,b,a,a])
#D=np.array([0,0,a,0])


#E=np.array([A,B,C,D])

E=np.array([A]*10)

'''
E[0][0]=a
E[0][1]=a

E[1][0]=a
E[1][1]=b
E[1][2]=b

E[2][0]=0
E[2][1]=b
E[2][2]=a
E[2][3]=a

E[3][0]=0
E[3][1]=0
E[3][2]=a

'''

np.fill_diagonal(E, [2, 2, 2])

for i in range(9):
    E[i][i+1]=-1


for j in range(9+1):
    E[j][j-1]=-1



 
 
   
#print(E)


#Aa=b

Einv=np.linalg.inv(E)

qq=(np.dot(Einv,bb))


plt.plot(q,qq)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("orange = exact solution, blue = matrix approximation, green = relative error")


aa=(f(q)-qq)/f(q)

plt.plot(np.log10(np.abs(aa))) #slutter ved 0.07
plt.xlim(0,1)

plt.show()
















