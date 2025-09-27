# Find the largest palindrome made from the product of two 3-digit numbers.

import array as ar


# method that i used to solve this problem is by using array and nested loop


def palindrome_method_1():  # this function give answer according to the problem statement
    arr = ar.array("i", [])
    for i in range(100, 1000):
        arr.append(i)

    arr2 = ar.array("i", [])
    for c in range(0, len(arr)):
        for j in arr:
            a = arr[c] * j
            if str(a) == str(a)[::-1]:
                arr2.append(a)

    print(max(arr2))


def palindrome_method_1_user_input():  # this function give answer according to the user range input
    x = int(input("Enter the starting range = "))
    y = int(input("Enter the ending range = "))
    arr = ar.array("i", [])
    for i in range(x, y + 1):
        arr.append(i)

    arr2 = ar.array("i", [])
    for c in range(0, len(arr)):
        for j in arr:
            a = arr[c] * j
            if str(a) == str(a)[::-1]:
                arr2.append(a)

    largest = max(arr2)

    print(largest)


# call the function palindrome_method_1() to get the output as per problem statment is 906609
# call the function palindrome_method_1_user_input() to get the output as per user input range


# another method to solve this problem without using array


def palindrome_method_2():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > largest_palindrome:
                    largest_palindrome = product

    print(largest_palindrome)  # output is 906609

# call the functon palindrome_method_2() to get the output as per problem statement is 906609


# another esaiest method to solve this problem without using array and nested loop by using generater expression and max function
def palindrome_method_3():
    largest_palindrome = max(
        i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[::-1]
    )

    print(largest_palindrome)  # output is 906609

# call the function palindrome_method_3() to get the output as per problem statement is 906609


# above all methods are correct and give the same output 906609
# you can use any method you like
# 