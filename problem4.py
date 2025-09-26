# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

import array as ar

arr = ar.array("i",[])
n = int(input("Enter the size of the array : "))
while len(arr) < n:
    arr.append(int(input("Enter the elements of the array: ")))

print("you enter the array : ", arr)
a = 0
target = 5

def pair_sum():
    for i in range(0,n):
        for j in arr:
            if arr[i] + j == target:
                return (i, arr.index(j))
            
print(pair_sum())



