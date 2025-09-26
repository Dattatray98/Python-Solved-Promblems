# Find the largest prime factor of a composite number

def prime_factors():
    n = int(input("Enter a number: "))
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1
    if n > 1:   
        print(n)

prime_factors()
