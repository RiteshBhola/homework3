from scipy import  integrate
import numpy as np
import math as m

def f(x):
	return m.exp(x)

Integral=integrate.romberg(f,0,1,show=True)
print(Integral)

