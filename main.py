"""Hacker Rank Challenges"""

#Program designed to calculate if current year is a leap year

def is_leap(year):

    #Leap year is instantiated as false
    leap = False

    #If year is evening divisible by 4, the value is changed to true
    if year % 4 == 0:
        leap = True

    #The majority of years that are divisible by 100 evening are not leap years
    if year % 100 == 0:
        leap = False

        #Years that are divisible by 100 and 400 are leap years
        if year % 400 == 0:
            leap = True


    return leap

year = int(input())
print(is_leap(year))