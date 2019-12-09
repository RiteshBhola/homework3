import math as m
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return m.sin(m.cos(m.exp(x)))


root=optimize.newton(f,-0.1)
print("Value of root",root)
print("Function value at root",f(root))
"""
output
Value of root 0.4515827052894548
Function value at root 6.123233995736766e-17

"""
