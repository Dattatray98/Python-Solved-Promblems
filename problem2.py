## Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million


import array as ar
a, b = 0,1

arr = ar.array("i", [])

while a < 4000000:
    if a % 2 == 0:
        print(a)
        arr.append(a)
    a ,b = b, a+b


print("sum of fibonacci series ", sum(arr))