import numpy as np
x = np.array([[2+2j, 4+1j, 6+3j], [6+1j, 8+1j, 10+4j]])
print(type(x))
print(x.shape)
print(x.dtype)
print(x)

print(x.reshape(3,2))