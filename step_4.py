import time
import pandas as pd
import numpy as np

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
    
def function1():
    """
Function 1:
The default method for finding intersection of two sets.
    """

    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
    
def function2():
    """
Function 2:
The method of finding intersection of two sets using built-in function of numpy.
    """
    
    start=time.time()
    verified_elements=np.intersect1d(all_elements,subset_elements)

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def function3():
    """
Function 3:
The method of finding intersection of two sets using data structure.
    """
    
    start=time.time()
    verified_elements=list(set(all_elements)&set(subset_elements))

    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def main():
    print(function1.__doc__)
    function1()
    print(function2.__doc__)
    function2()
    print(function3.__doc__)
    function3()

if __name__ == "__main__":
    main()