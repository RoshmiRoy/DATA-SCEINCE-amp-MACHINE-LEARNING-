import numpy as np
array = np.random.randint(10, size=(3, 3))
print(array)
#i) inverse
array=np.linalg.inv(array)
print("Inverse array is ")
print(array)
print()
#2)rank of matrix
print("The Rank of a Matrix: ", np.linalg.matrix_rank(array))
#3)) Determinant
det = np.linalg.det(array)
print(int(det))
#4) transform matrix into 1D array
flat_array = array.flatten()
print('1D Array:')
print(flat_array)
#5) eigen values and vectors
w,v=np.linalg.eig(array)
print("eigen value:",w)
print("eigen vector:",v)