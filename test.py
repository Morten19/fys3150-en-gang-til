



import numpy as np
import matplotlib.pyplot as plt




e=np.loadtxt("data.txt")

f=(e[:,0])

g=(e[:,1])

plt.plot(f,g)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.show()

