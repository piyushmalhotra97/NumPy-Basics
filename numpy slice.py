import numpy as np

x = np.arange(10,20)
print(x)
s = slice(2,7,2) #Start -> 2, End at 7, inc 2
print(x[s])
#or we can write
print(x[2:7:2])
