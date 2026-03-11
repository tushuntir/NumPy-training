import numpy as np

arr = np.array([1,2,3,4])
arr4 = np.array([1,2,3,4])

newarr =  arr.astype("i")
newar = arr4.astype(bool)

print(arr.dtype)
print(arr4.dtype)
print(newar.dtype)  