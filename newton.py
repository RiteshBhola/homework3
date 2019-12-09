import math as m
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return m.sin(m.cos(m.exp(x)))
	
def fprime(x):
	return -m.exp(x)*m.sin(m.exp(x))*m.cos(m.cos(m.exp(x)))


root=optimize.newton(f,-0.1,fprime)
print("Value of root",root)
print("Function value at root",f(root))
"""
The newton raphsion gave a different root than bisection method when -1 is initial guess.
for -1
Value of root 9.179198883610521
Function value at root -5.921874465645097e-12

The newton raphsion gave same root as bisection method when -0.1 is initial guess.
for -0.1
Value of root 0.4515827052894549
Function value at root 6.123233995736766e-17

The method drives away or toward a root depending upon the initial guess and value of derivative at the initial guess.
"""
