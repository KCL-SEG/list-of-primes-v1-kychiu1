"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    counter = 2
    while len(list) < number_of_primes:
        # check if a number is prime
        isPrime = True
        j = 0
        while isPrime and j < len(list):
            if counter % list[j]== 0:
                isPrime = False
            j += 1

        if isPrime:
            list.append(counter)
        counter += 1
    return list
