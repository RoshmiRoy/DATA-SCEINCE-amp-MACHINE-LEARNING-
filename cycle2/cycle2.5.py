import numpy as np
x=np.arange(0,30,2)
print(x)
first_element2 = x[2:9:2]
print(first_element2)
s = slice(2, 9, 2)
print(x[s])
print(x[-3:30])
