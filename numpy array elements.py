import numpy as np

x = np.array([[0,1,2],[3,4,5],[5,6,7],[7,8,9]])
print(x)

print(x[...,[0,2]])

print(x[2,...])

print(x[[1,2],...])


