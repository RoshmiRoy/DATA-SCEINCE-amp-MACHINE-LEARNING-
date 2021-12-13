import numpy as np
from numpy import diag
from numpy import dot
from scipy.linalg import svd
a=np.array([[1, 2,3], [4, 5, 6], [7, 8,9]])


print(a)
# SVD
U, s, VT = svd(a)
print(U)
print(s)
print(VT)
# create n x n Sigma matrix
Sigma = diag(s)
# reconstruct matrix
B = U.dot(Sigma.dot(VT))
print(B)

