This case task was to allow hackerrank an ability to input two strings.  The first being a user searchable case.  The second case being a string to be iterated from the first string.

I had to do research on how to allow hackerrank to input a particular string whch happend to be the input() method and i tied them to the variables the program was looking for.

Importing re allowed me the ability to use re.finditer method which searches a variable with a specified case.  If the case doesn't exist within the varable the return value is -1, -1.
Otherwise a list is created within the assigned variable.

An if statement is instantiated to check the list if the user search case exists.  If it does not, the program returns -1, -1 and ends the program right there.

If there is a value for the case then the next portion of the if statement is executed which gives the locations for each case that is a part of the list which would be a start and an end location.
Additionally, -1 had to be included on the end case because the end scope is always one more than what the case actually is.
