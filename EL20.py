# n! means n  (n  1)  ...  3  2  1

# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


#############End of instructions#########

#keeps track of the programs loop progress

PC = 0 

#this is the variable that we use to return the final answer
final = 0

# this is the number that we want the factorial of
factorial = 100

#this is the sum of the actual digits
factorialsum = 0

#this is the multiplied for of the factorial
factorialmulti = 0

#this loop figures out the what the factorial of the number that we want is 
while factorial > 0:
	

	#preforms the maintance on the loop
	factorial = factorial - 1
# this loop adds the digits of that number together for our final answer

