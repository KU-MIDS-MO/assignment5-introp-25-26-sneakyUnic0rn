"""
##task3

Write a function `approx_real_root(coeffs, interval)` that:

- receives a list `coeffs` of four numbers representing a cubic polynomial,starting with the coefficient of the free term and finishing with the coefficient of x^3
- receives a tuple `interval = (a, b)` with `a < b`,
- assumes that **the polynomial has exactly one real root inside this interval**,
- computes and returns a floating-point approximation of that root,
- and ensures that the approximation is accurate to at least **1×10⁻⁹** in absolute error
---

"""
import numpy as np

def approx_real_root(coeffs, interval):
    #get reverse coefficients
    reversed_coeffs = coeffs[::-1]
    
    #find all roots
    all_roots = np.roots(reversed_coeffs)
    
    #keep only real roots
    real_roots = [r.real for r in all_roots if np.isreal(r)]
    
    #return one in the interval
    a, b = interval
    for r in real_roots:
        if a <= r <= b:
            return r
        
    