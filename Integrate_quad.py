from scipy import  integrate
import numpy as np
import math as m

def f(x):
	return m.exp(x)

Integral=integrate.quad(f,0,1)
print(Integral)

