from scipy import  integrate
import numpy as np
import math as m

def f(x):
	return m.exp(x)

x=np.linspace(0,1,100)
f2=np.vectorize(f)
y=f2(x)
Integral=integrate.simps(y,x,even='first')
print(Integral)

