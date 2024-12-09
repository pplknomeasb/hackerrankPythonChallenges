"""Hacker Rank Challenges"""
import random

"""2 Random numbers called"""
def calculator(caseNumber):

    #Prints the square root value for every number between 0 and the generated number

    for currentNumber in range(0, caseNumber):
        print(f"{currentNumber} squared equals {currentNumber ** 2}")

if __name__ == "__main__":

    # Randomized a number between 0 and 30 for 2 Variables
    number1 = random.randint(0, 20)

    print(f"The generated number is {number1}")

    print()

    #Sends the two random numbers to the calculator function
    calculator(number1)