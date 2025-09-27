# What is the smallest number divisible by each of the numbers 1 to 20? 

# method 1 is by using nested for loop and it used by me.
def smallest_divisible_method_1():
    for i in range(1, 1000000000):
        if_divsible = True
        for j in range(1, 21):
            if i % j != 0:
                if_divsible = False
                break
        if if_divsible:
            print(i)

smallest_divisible_method_1()

# method 2 is by using while loop and all() function and it was i explored by chatgpt.
def smallest_divisible_method_2():
    n = 1 
    while True:
        if all(n % i == 0 for i in range(1, 21)):
            print(n)
            break
        n += 20 