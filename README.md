The task here is to calculate which years are leap years on the gregorian calendar.  

The problems I experienced were differencing the years that were not leap years.

All leap years can evenly be divided by 4 but there are years divisible by 4 that are not leap years and some of those numbers are divisible by 4 and 100.
Those years that are leap years must be evening divisible by 400.

Instead of including all of the calculations in the same if loop, I changed all years divisible by 4 into a leap year.
I then checked if the years could also be divisible by 100.  If that was true I changed the value to false.
I embeded an if loop inside that loop to check if any of those years were also divisible by 400
If so, i changed the result back to true for it to be a leap year.
