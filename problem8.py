# Find the 10001st prime


# method 1 : i was used this method, in this method i was used nested for loops and if statements and math.sqrt() function
import math

def prime_number():
    c = 0

    for i in range(2, 140000):
        is_prime = True
        b = math.sqrt(i)
        for a in range(2, int(b) + 1):
            if i % a == 0:
                is_prime = False
                break
        if is_prime:
            c += 1

        if is_prime and c == 10001:
            print(i)


prime_number()    # calling the function prime_number() to find 10001st prime number.