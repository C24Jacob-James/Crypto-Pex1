""" CryptoPex1.py
Name: Jacob M. James
Date: 22 March 2024
Purpose: Factor large numbers using Brute Force, Pollards_rho, and dixons
Documentation: I used Chat GPT to give me an outline for the start of the project. 
    I used this website to give me the code for Dixon's algorithm: https://www.geeksforgeeks.org/dixons-factorization-method-with-implementation/
    I then asked ChatGPT to make the code and variables more readable. I asked Chat GPT to create the timer functionality for me for all of the 
    algorithms and I asked it to refactor Dixon' for me.
"""

import numpy as np
import time
import sympy

maxTime = 120  # maximum time each algorithm can run in seconds

def brute_force(toFactor):
    """
    Brute force algorithm for integer factorization.
    """
    print("Brute force factoring")

    start_time = time.time()  # Start timer

    for n in range(2, int(np.sqrt(toFactor)) + 1):
        if toFactor % n == 0:
            print("Found a factor =", n)
            end_time = time.time()  # End timer
            print("Time taken:", end_time - start_time, "seconds")
            return

        # Check elapsed time and break if it exceeds max time limit
        if time.time() - start_time > maxTime:
            print("Time limit of", maxTime,"seconds reached! Exiting...")
            return

    end_time = time.time()  # End timer
    print("No factor found!! >_<")
    print("Time taken:", end_time - start_time, "seconds")
    

def pollards_rho(toFactor):
    """
    Pollard's Rho algorithm for integer factorization.
    """

    print("Pollard’s Rho")

    tortoise, hare = 2, 2
    d = 1

    start_time = time.time()  # Start timer

    while d == 1:
        tortoise = pollardFunc(tortoise, toFactor)
        hare = pollardFunc(pollardFunc(hare, toFactor), toFactor)
        absoluteVal = np.abs(tortoise - hare)
        d = np.gcd(toFactor, absoluteVal)

        # Check elapsed time and break if it exceeds max time limit 
        if time.time() - start_time > maxTime:
            print("Time limit of", maxTime,"seconds reached! Exiting...")
            return

        if 1 < d and d < toFactor:
            print("Found a factor =", d)
            print("tortoise =", tortoise, ",   hare =", hare)
    
        if d == toFactor:
            print("No factor found!! >_<\n") 
            return

    end_time = time.time()  # End timer
    print("Time taken:", end_time - start_time, "seconds")
    

def pollardFunc(x, toFactor):
    return (x**2 + 1) % toFactor
    
## Begin Dixon's
import numpy as np
from math import sqrt, ceil, gcd
import time

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def factorize(n, factor_base):
    factors = [0] * len(factor_base)
    for i, prime in enumerate(factor_base):
        while n % prime == 0:
            n //= prime
            factors[i] += 1
    return factors

def dixon_main(n, factor_base_size):
    # Generate factor base using primes
    factor_base = generate_primes(factor_base_size)
    
    # Store timing information
    start_time = time.time()

    # Starting from the ceil of the root
    # of the given number N
    start = int(ceil(sqrt(n)))

    # Output format
    print("x * y === x^2 mod N", end="")
    for prime in factor_base:
        print(f" {prime}", end="")
    print()

    # For every number from the square root 
    # Till N
    for i in range(start, n):
        # Storing the related squares
        pairs = []

        # Finding the related squares 
        for j in range(len(factor_base)):
            lhs = i**2 % n
            rhs = factor_base[j]**2 % n
            
            # If the two numbers are the 
            # related squares, then append
            # them to the array 
            if(lhs == rhs):
                pairs.append([i, factor_base[j]])

        # Output the pairs
        for pair in pairs:
            factors = factorize(pair[0] * pair[1], factor_base)
            print(f"{pair[0]} * {pair[1]} === {i}", end="")
            for factor in factors:
                print(f" {factor}", end="")
            print()

        # Check if any factors found
        for pair in pairs:
            factor = gcd(pair[0] - pair[1], n)
            if factor != 1 and factor != n:
                print(f"Found a factor = {factor}")
                break

        # Check if two minutes have elapsed
        if time.time() - start_time > maxTime:
            print("Time limit exceeded! Exiting...")
            return

    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    print(f"It took {elapsed_time:.2f} seconds.")


# Example usage:
# n = 124076833
# factor_base_size = 10
# dixon_main(n, factor_base_size)





def main():
    
    toContinue = "y"
    
    # # Print title and class num
    print("\n\nPEX1 - Factoring! - by Cadet Jacob M. James (Awesomesauce)")
    print("CyS 431\n")
    
    while toContinue == "y":

        # Prompt for a number to factor
        toFactor = int(input("Enter a number to factor: "))
        print()

        # toFactor = 10003199**2    # used for testing

        # Start with the brute force factoring
        brute_force(toFactor)
        print()


        # Run Pollard's Rho
        pollards_rho(toFactor)

        

        # Run Dixon's
        print("\nDixon's Algorithm")
        factorBase = int(input("Enter # of factors in factor base:"))
        dixon_main(toFactor, factorBase)


        toContinue = input("Do you want to try another number? (y/n): ")

        while toContinue != "y" and toContinue != "n":
            print("I'm sorry. Please respond with either a 'y' or an 'n'.")
            toContinue = input("Do you want to try another number? (y/n): ")



        pass

if __name__ == "__main__":
    main()
