## What is the difference between the sum of the squares and the square of the sums?




# method 1 to find the difference between the sum of the squares and the square of the sum which is used and created by me 
import array as ar

arr = ar.array("i", [])
arr2 = ar.array("i", range(1, 101))

def Sum_Square_differnece_method_1():
    for i in range(1, 101):
        a = i*i
        arr.append(a)


    b = sum(arr)
    c = sum(arr2)
    d = c*c
    print(d-b)


# method 2 by using the formula of find the sum of first n natural numbers and the sum of square of first n natural numbers


def Sum_Square_differnece_method_2():
     n = 100
     s = n*(n+1)//2
     sq = n*(n+1)*(2*n + 1)//6
     square = s * s
     print(square - sq)



# method 3 by using one line with python build-ins

def Sum_Square_differnece_method_3():
    a = sum(i*i for i in range(1, 101))
    b = sum(range(1,101)) ** 2
    print(b-a)

Sum_Square_differnece_method_3()


