""" CryptoPex1.py
Name: Jacob M. James
Date: 22 March 2024
Purpose: Factor large numbers using Brute Force, Pollards_rho, and dixons
Documentation: I used Chat GPT to give me the start of the project. I just asked it for the skeleton code and none of the implementations. 
"""

import math

def brute_force(toFactor):
    """
    Brute force algorithm for integer factorization.
    """
    # base case is if n % toFactor == 0

    for n in range(2,int(math.sqrt(toFactor)) + 1):
        if toFactor % n == 0:
            print("Found a factor =", n)
            return
        
    print("No factor found!! >_<")
    

def pollards_rho(toFactor):
    """
    Pollard's Rho algorithm for integer factorization.
    """
    # Implementation goes here
    pass

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
    pass

if __name__ == "__main__":
    main()
