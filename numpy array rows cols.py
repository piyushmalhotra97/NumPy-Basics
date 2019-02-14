import numpy as np

x = np.array([[0,1,2,3],[3,4,5,6],[6,7,8,9],[9,10,11,12]])
print(x)
rows = np.array([[0,0],[3,3]])
print(rows)
cols = np.array([[0,3],[0,3]])
print(cols)
y = x[rows,cols]
print(y)
