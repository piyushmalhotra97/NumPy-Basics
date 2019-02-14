#NumPy lists reshape

import numpy as np

a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(4,3,2)
print(b)
print(b[3][0][1])
