"""
##task 1

Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

- receives a 2D NumPy array `A`,
- computes the range (maximum minus minimum) of each column,
- create a bar plot showing the ranges of all columns,
- saves the plot as a PDF file,
- and returns a 1D NumPy array containiing the column ranges.

---

"""

import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    #init an empty list for ranges
    a_range = []
    #use loop to check through columns
    for i in range(A.shape[1]):
        #extract the i-th column
        col = A[:, i]
        #find max number in column
        max_num = col.max()
        #find min number in column
        min_num = col.min()
        #calc the range
        range_num = max_num - min_num
        #append range in list
        a_range.append(range_num)
        
        
    #create category for columns
    categories = np.arange(1, A.shape[1] + 1)
    
    #generate bar chhart using plt.bar
    plt.bar(categories, a_range)
    plt.xlabel("Column")
    plt.ylabel("Range")
    plt.title("Column Ranges")
    plt.savefig(filename)
    plt.show()
    
    return np.array(a_range)
        
        
        
