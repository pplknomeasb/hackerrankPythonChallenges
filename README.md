It is asked to put together a string value from a list of integers.  The program is to read a number and generate a string between 1 and that value. 

Converting an integer to string was the first complication.  I instantiated a string place as "" first in order to have a string to build into.  Creating a for loop starting at 1 was the next complication.  The reason the loop started at 1 is because 0 is to not be included in the string built.

The last number in the string was not added to the string because once the loop reached that number the loop ended and the string did not add the number that was originally selected.  Once the loop ended, I made sure to add one to the current number and add it to the string so that the original number would be added to the string output.
