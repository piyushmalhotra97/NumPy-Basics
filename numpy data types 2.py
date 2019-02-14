#Data types List 2

import numpy as np
l = [[1,2,3],[4,5,6],[7,8,9]]
print(l)
#print(np.array(l , ndmin = 5))
print(np.array(l , dtype = complex))
print(np.array(l , dtype = int))
print(np.array(l , dtype = float))

dt = np.dtype(np.int32)
print(dt)
dt = np.dtype('i1')
print(dt)
dt = np.dtype('i2')
print(dt)
dt = np.dtype('i4')
print(dt)
dt = np.dtype('i8')
print(dt)
