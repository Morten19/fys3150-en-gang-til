


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


q=np.array([1/100,
2/100,
3/100,
4/100,
5/100,
6/100,
7/100,
8/100,
9/100,
10/100,
11/100,
12/100,
13/100,
14/100,
15/100,
16/100,
17/100,
18/100,
19/100,
20/100,
21/100,
22/100,
23/100,
24/100,
25/100,
26/100,
27/100,
28/100,
29/100,
30/100,
31/100,
32/100,
33/100,
34/100,
35/100,
36/100,
37/100,
38/100,
39/100,
40/100,
41/100,
42/100,
43/100,
44/100,
45/100,
46/100,
47/100,
48/100,
49/100,
50/100,
51/100,
52/100,
53/100,
54/100,
55/100,
56/100,
57/100,
58/100,
59/100,
60/100,
61/100,
62/100,
63/100,
64/100,
65/100,
66/100,
67/100,
68/100,
69/100,
70/100,
71/100,
72/100,
73/100,
74/100,
75/100,
76/100,
77/100,
78/100,
79/100,
80/100,
81/100,
82/100,
83/100,
84/100,
85/100,
86/100,
87/100,
88/100,
89/100,
90/100,
91/100,
92/100,
93/100,
94/100,
95/100,
96/100,
97/100,
98/100,
99/100,
100/100])

list1=f(q)

bb=list1 #lengde 10

plt.plot(q,f(q))


#Aa = b


a = -1
b=2
c=-1


nn=100

A = np.linspace(0,0,nn)
B = np.linspace(0,0,nn)
C = np.linspace(0,0,nn)
D = np.linspace(0,0,nn)

#A=np.array([a,a,0,0])
#B=np.array([a,b,b,0])
#C=np.array([0,b,a,a])
#D=np.array([0,0,a,0])


#E=np.array([A,B,C,D])

E=np.array([A]*100)

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

qqq=[]
for kk in range(101):
    qqq.append((3*kk-2))


for i in range(99): #15-1
    E[i][i+1]=-1









qq=[]
for k in range(101):
    qq.append((3*k-1))
    
    
for j in range(100): #for 15 samme som array
    E[j][j-1]=-1





#print(qq)
 #3*i-1
   


Einv=np.linalg.inv(E)

qq=(np.dot(Einv,bb))
plt.plot(q,qq)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("n=100, orange = exact solution, blue = matrix approximation, green = logarithm of the absolute error")


aa=(f(q)-qq)

plt.plot(np.log10(np.abs(aa))) #slutter ved 0.07
plt.xlim(0,1)

plt.show()






