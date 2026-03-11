import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([[1,2,3], [3,2,1]])
arr3 = np.array([[[1,2,3], [2,5,8], [9,7,8], [67,67,67]]])

# print(arr[1]+ arr[2])
# print(f"2nd elements in the 1st row is: {arr2[0,1]}")
# print(f"1st element in the 2nd row is {arr2[1,0]}")

# print(arr3[-1,-1,-1])

print(arr[::2])
print(arr2[1, :-1])
print(arr2[0:2, 2])