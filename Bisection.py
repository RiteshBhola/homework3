import math as m
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return m.sin(m.cos(m.exp(x)))

#f2=np.vectorize(f)
#x=np.linspace(-1,1,100)

#plt.plot(x,f2(x),'b', lw=3)
#plt.show()
root=optimize.bisect(f,-1,1)
print("Value of root",root)
print("Function value at root",f(root))
"""
the function is not 0 at root instead -2.4313271915891353e-12(a very small no.). The root given by bisection is not the real root, it is the closest it can get to the root within given tolerence.
"""
