import numpy as np 

arr = np.array([1,2,3,4,5])
y = arr.copy()
x = arr.view()
arr[0] = 42


print(arr)
print(x.base)
print(y.base)