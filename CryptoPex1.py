""" CryptoPex1.py
Name: Jacob M. James
Date: 22 March 2024
Purpose: Factor large numbers using Brute Force, Pollards_rho, and dixons
Documentation: I used Chat GPT to give me the start of the project. I just asked it for the skeleton code and none of the implementations. 
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
        hare = pollardFunc(hare, toFactor)
        hare = pollardFunc(hare, toFactor)
        absoluteVal = np.abs(tortoise - hare)
        d = np.gcd(toFactor, absoluteVal)

        if 1 < d and d < toFactor:
            print("Found a factor =", d)
    
        if d == toFactor:
            print("No factor found!! >_<\n") 
    

def pollardFunc(x, toFactor):
    x2 = x**2 + 1
    toReturn = x2 % toFactor
    return toReturn

def dixons_factorization(toFactor):
    """
    Dixon's factorization algorithm.
    """
    # Implementation goes here
    pass

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

    print()
    pass

if __name__ == "__main__":
    main()
