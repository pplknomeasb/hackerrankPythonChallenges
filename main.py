"""Hacker Rank Challenges"""
import random

"""2 Random numbers called"""
def calculator(caseNumber1, caseNumber2):

    # Simple math code for addition, subtraction, and multiplication
    print(f"{caseNumber1}+{caseNumber2} = {caseNumber1+caseNumber2}")
    print(f"{caseNumber1}-{caseNumber2} = {caseNumber1-caseNumber2}")
    print(f"{caseNumber1}*{caseNumber2} = {caseNumber1*caseNumber2}")

if __name__ == "__main__":

    # Randomized a number between 0 and 30 for 2 Variables
    number1 = random.randint(0, 20)
    number2 = random.randint(0, 20)
    print(number1)
    print(number2)
    print()

    #Sends the two random numbers to the calculator function
    calculator(number1, number2)