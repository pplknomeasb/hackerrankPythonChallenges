"""Hacker Rank Challenges"""
import random

#Random number called
def printedValue(caseNumber):

    #Creating a string holder
    printedNumber = ""

    #Range starts at 1 because thats the number we want to start the string with
    for currentNumber in range(1, caseNumber):

        #Each loop through builds a string value adding current place holder
        printedNumber = printedNumber + str(currentNumber)

    #The loop doesn't pring the final value.  Adds one to catch the last digit
    printedNumber = printedNumber + str(currentNumber + 1)

    print(printedNumber)


if __name__ == "__main__":

    # Randomized a number between 0 and 30 for 2 Variables
    number1 = random.randint(0, 20)

    print(f"The generated number is {number1}")

    print()

    #Sends the random number to the calculator function
    printedValue(number1)