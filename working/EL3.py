#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#while test <= desired numer
#store all the factors into an array
#while greater then zero and cont == true
# then after putting them all in the array
#Sort it
#then go from highest to lowest return the first prime



#this keeps the loop going
cont = 1
# The next number to retrieve from the array
PC = 0
#What is the largest prime factor of the number 600851475143 ?

#This keeps track of what the largest prime variable is
largestprime = 0

#this is our limiting fator that keeps track of the value we want the prime factors of
number = 600851475143

#this keeps the value of the array to check against the highest
arrayval = 0

#this varialbe keeps track of the last highest prime (that way we have a way of catching it after it went over
secondhighest = 0
#prebuilds the list of primes that we need for the program
prime = primes(1000000000)
#600851475143
while cont == 1:
	#retrieve the next value to test out of the array
	arrayval = prime[PC]
	#check if the number is greater than the number if not then it adds it if so then it stops the loop
	if arrayval >= number:
		cont = 0
	#check if it is a factor of the number
	if arrayval % number == 0:
		#then it is the new highest prime and set it as that
		print "New highest number"
		highestprime = arrayval
	#maintains the loop
	PC = PC + 1
print largestprime
