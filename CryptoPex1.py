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

def generate_factor_base(factor_base_size):
    print("Done generating factor base.")
    return list(sympy.primerange(2, factor_base_size + 2))

def dixons_algorithm_single_equations(toFactor, factor_base):

    print("1", toFactor, "===", toFactor, end=" ")
    for p in factor_base:
        x = int(np.ceil(np.sqrt(p * toFactor)))
        y_square = x ** 2 - toFactor
        if sympy.isprime(y_square):
            y = int(np.sqrt(y_square))
            print(x, y, end=" ")
            print(np.sum([int(digit) for digit in str(x)]), end=" ")
            print(np.sum([int(digit) for digit in str(y)]), end=" ")
            for i in range(len(str(x))):
                print(str(x).count(str(i)), end=" ")
            for i in range(len(str(y))):
                print(str(y).count(str(i)), end=" ")
            print()

# Timing mechanism with retries
def dixon_main(toFactor, factor_base_size, retries=3, timeout=120):
    attempts = 0
    while attempts < retries:
        try:
            start_time = time.time()
            factor_base = generate_factor_base(int(factor_base_size))
            dixons_algorithm_single_equations(toFactor, factor_base)
            end_time = time.time()
            print("Total time taken:", end_time - start_time, "seconds")
            return
        except Exception as e:
            print("An error occurred:", e)
            attempts += 1
    print("Factoring failed after", retries, "attempts.")


# Example usage:
# Assume you have a FactorBase class for factorization
# factor_base = FactorBase(30)  # Assuming the factor base will be no larger than 30
# k = ...  # Some integer
# n = ...  # The number to factorize

# Call Dixon's algorithm
# factors = dixons_algorithm(k, n, factor_base)
# print("Factors:", factors)



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
        factorBase = input("Enter # of factors in factor base:")
        dixon_main(toFactor, factorBase)
        print()

        toContinue = input("Do you want to try another number? (y/n): ")

        while toContinue != "y" and toContinue != "n":
            print("I'm sorry. Please respond with either a 'y' or an 'n'.")
            toContinue = input("Do you want to try another number? (y/n): ")



        pass

if __name__ == "__main__":
    main()
