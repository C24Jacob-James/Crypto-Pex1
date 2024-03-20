""" CryptoPex1.py
Name: Jacob M. James
Date: 22 March 2024
Purpose: Factor large numbers using Brute Force, Pollards_rho, and dixons
Documentation: I used Chat GPT to give me the start of the project. I just asked it for the skeleton code and none of the implementations. 
    I used this website to give me the code for Dixon's algorithm: https://www.geeksforgeeks.org/dixons-factorization-method-with-implementation/

"""

import numpy as np



def brute_force(toFactor):
    """
    Brute force algorithm for integer factorization.
    """
    # base case is if n % toFactor == 0

    print("Brute force factoring")

    for n in range(2,int(np.sqrt(toFactor)) + 1):
        if toFactor % n == 0:
            print("Found a factor =", n) 
            return
        
    print("No factor found!! >_<\n")
    

def pollards_rho(toFactor):
    """
    Pollard's Rho algorithm for integer factorization.
    """

    print("Pollard’s Rho")

    tortoise, hare = 2, 2
    d = 1

    while d == 1:
        tortoise = pollardFunc(tortoise, toFactor)
        hare = pollardFunc(pollardFunc(hare, toFactor), toFactor)
        absoluteVal = np.abs(tortoise - hare)
        d = np.gcd(toFactor, absoluteVal)

        if 1 < d and d < toFactor:
            print("Found a factor =", d)
            print("tortoise =", tortoise, ",   hare =", hare)
    
        if d == toFactor:
            print("No factor found!! >_<\n") 
    

def pollardFunc(x, toFactor):
    return (x**2 + 1) % toFactor
    

import numpy as np

def dixons_factorization(toFactor):
    """
    Dixon's factorization algorithm.
    """
    # Factor base for the given number
    factor_base = [2, 3, 5, 7]

    # Starting from the ceil of the square root
    # of the given number
    start_point = int(np.sqrt(toFactor))

    # Storing the related squares
    related_pairs = []

    # For every number from the square root 
    # Till the given number
    for i in range(start_point, toFactor):

        # Finding the related squares 
        for j in range(len(factor_base)):
            lhs = i**2 % toFactor
            rhs = factor_base[j]**2 % toFactor
            
            # If the two numbers are the 
            # related squares, then append
            # them to the array 
            if(lhs == rhs):
                related_pairs.append([i, factor_base[j]])

    factors = []

    # For every pair in the array, compute the 
    # GCD such that 
    for i in range(len(related_pairs)):
        factor = np.gcd(related_pairs[i][0] - related_pairs[i][1], toFactor)
        
        # If we find a factor other than 1, then 
        # appending it to the final factor array
        if(factor != 1):
            factors.append(factor)

    unique_factors = np.array(factors)

    # Returning the unique factors in the array
    print(np.unique(unique_factors))


def main():
    # Print title and class num
    print("\n\nPEX1 - Factoring! - by Cadet Jacob M. James (Awesomesauce)")
    print("CyS 431\n")
    
    # Prompt for a number to factor
    toFactor = int(input("Enter a number to factor: "))

    # Start with the brute force factoring
    brute_force(toFactor)
    print()


    # Run Pollard's Rho
    pollards_rho(toFactor)


    dixons_factorization(toFactor)
    print()
    pass

if __name__ == "__main__":
    main()
