import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows = len(a)
    cols = len(a[0])

    x, y = new_shape

    if rows*cols != x*y:
        return []
    
    mat = []

    for i in range(rows):
        mat += a[i]

    reshaped_matrix = []
    
    reshaped_matrix = [mat[i*y:(i+1)*y] for i in range(x)]
      
    return reshaped_matrix