"""Hacker Rank Challenges"""
import random

"""Randomized Number brought into function to check for even or odd number"""
def evenOddCheck(checkNumber):

    """Modulator checks if number returns Remainder"""
    """Even numbers return 0. Odd numbers return > 0 remainder"""
    if checkNumber % 2 == 0:

        """2, 4, and anything greater than 20 is to return not Weird"""
        if (checkNumber >= 2 and checkNumber < 5) or (checkNumber >= 20):
            print("Not Weird")
        else:

            """Any even number between 5 and 19 is to return Weird"""
            print("Weird")
    else:

        """Prints Weird if any number returns a remainder with %"""
        print("Weird")

if __name__ == "__main__":

    """Randomized a number between 0 and 30"""
    number = random.randint(0, 30)
    print(number)

    """Calls evenOddCheck class and sends the random number"""
    evenOddCheck(number)