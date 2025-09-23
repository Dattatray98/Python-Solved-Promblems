## Question : Find the sum of all the multiples of 3 or 5 below 1000.


# The method i have used initialy 
import array 

arr = array.array("i", range(1, 1000))


arr2 = array.array("i", [])

for i in arr:
    if i % 3 == 0 or i % 5 == 0:
        arr2.append(i)
        
    i += 1

print(arr2)
print(sum(arr2))

# other 2 easist methods that i find out :

## method 1 : using list 
numbers = [i for i in range(1,1000) if i% 3 == 0 or i % 5 == 0]
print(numbers)
print(sum(numbers))


## method 2 : directly doning sum

total = sum(i for i in range(1, 1000) if i%3 == 0 or i%5 == 0)
print(total)