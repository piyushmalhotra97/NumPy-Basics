#NumPy lists shape

import numpy as np
l = [[1,2,3],[4,5,6]]
a = np.array(l)
print(a)
print(a.shape)
a.shape = (3,2)
print(a)
