#NumPy lists range

import numpy as np
l = [[1,2,3],[4,5,6]]
a = np.array(l)
print(a)
print(a.shape)
a.shape = (3,2)
print(a)

a = np.arange(20)
a.shape = (4,5)
print(a)
print(a.ndim)

a = np.arange(1,20)
print(a)
print(a.ndim)

a = np.arange(1,20,2)
print(a)
print(a.ndim)

a = np.arange(24)
print(a.ndim)
