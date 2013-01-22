# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

#finds the expponent of 2^1000 and returns the sum of the numbers

#Sum of it all
Sum = 0

#good code documents itself(;
Base = 2
expponent = 1000

#The great keeper of time
PC = 1

#The substring selectors
x = 0 
y = 1 

#Calculates the number after the power
#LOL I cant maths
SecondaryNumber = Base ** expponent

#returns the length of the exponent calculated
Length = len(str(SecondaryNumber))
SecondaryNumberstr = str(SecondaryNumber)

#takes the types and calculates the sum
while y <= Length:
	SNSTR = SecondaryNumberstr[x:y]
        SNINT = int(SNSTR)
        Sum = Sum + SNINT 
	#Increases both of the counters by one
	x = x + 1
	y = y + 1
print Sum
