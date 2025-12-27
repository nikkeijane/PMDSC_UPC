import numpy as np

# Printing only True values
# arr = np.array([41,42,42,44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)

#Creating the filter array
# arr = np.array([41,42,43,44])

# filter_arr = []

# for element in arr:
#     if element > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(newarr)
# print(arr)

#Create a filter array that will return only even elements 
# from the original array

arr = np.array([1,2,3,4,5,6,7])

filter_arr = []

for x in arr:
    if x % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(newarr)