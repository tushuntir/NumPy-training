import numpy as np

arr = np.array([1,2,3,4,5])
arrt = np.array((1,2,3,4,5))

print(arr)
print(type(arr))
print(arrt)
print(type(arrt))



arr0 = np.array(42)
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3], [3,2,1]])
arr3 = np.array([[[1,2,3], [3,2,1], [67,67,67]]])
arrndim = np.array([1,2,3,4,5], ndmin=5)


print(arr0)
print(arr1)
print(arr2)
print(arr3)
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arrndim.ndim)