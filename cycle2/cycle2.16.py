import numpy as np
m1 = np.array([[1,2],[2,5]])
m2=m1.transpose()
print(m2)
comparison = m1 == m2
equal_arrays = comparison.all()
  
print(equal_arrays)
#checking itis skew symmetirc
a=(m1.transpose() == -m1).all()
print(a)