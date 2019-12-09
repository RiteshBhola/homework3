import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline as spline
from scipy.interpolate import lagrange


x=np.array([0,1,2,3,4,5])
y=np.array([1.0,2.0,1.0,0.5,4.0,8.0])
"""
linear splne
"""
y_spl=spline(x,y,None,[None,None],1)
xs = np.linspace(0,5, 1000)
plt.plot(xs, y_spl(xs), 'g', lw=3,label="linear spline")

y_spl=spline(x,y,None,[None,None],2)
plt.plot(xs, y_spl(xs), 'b', lw=3,label="quadratic spline")

y_spl=spline(x,y,None,[None,None],3)
plt.plot(xs, y_spl(xs), 'm', lw=3,label="cubic spline")

y_lagrange=lagrange(x,y)
plt.plot(xs, y_lagrange(xs), 'c', lw=3,label="lagrange polynomial")

plt.plot(x,y,'ro',ms=5,label="Data points")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
