"""
##task2

Write a function `detect_turning_points(signal, filename="turning_points.pdf")` that:

- receives a 1D NumPy array representing a signal
- identifies all indices where the direction of the signal changes  
  (i.e., where the discrete difference changes sign),
- plots the signal and mark these turning points,
- saves the figure as a PDF file,
- and returns a NumPy array containing the indices of the detected points

---

"""

import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    #compute difference
    #np.diff computes the difference between consecutive elements of an array.
    diff = np.diff(signal)
    
    #use signs to find out signal direction
    direction = np.sign(diff)
    
    #decide turning points based on signs
    turning_points = np.where(direction[1:] != direction[:-1]) [0] + 1
    
    #plot the signal
    x = np.arange(len(signal))
    plt.plot(x, signal, marker="o", label="Signal")
    
    #mark the turning points
    plt.scatter(turning_points, signal[turning_points], s=100, marker="X", label="Turning Points", color="red")
    
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Turning Points")
    plt.legend()
    plt.savefig(filename)
    
    return turning_points
    

"""

np.diff(array) computes the difference between consecutive elements of an array
np.sign(array) returns the signs of each element of an array
np.where(condition) returns indices where condition is true and can handle multiple dimension
e.g., 
arr = np.array([False, True, True, False, True])
np.where(arr)
output : (array[1,2,4],)
np.where(arr)[0]
output : array[1,2,4]

"""