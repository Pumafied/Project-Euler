#The prime factors of 13195 are 5, 7, 13 and 29.
<<<<<<< HEAD
#What is the largest prime factor of the number 600851475143 ?

#this keeps the loop going
cont = 1

# The next number to retrieve from the array
PC = 0
=======

#What is the largest prime factor of the number 600851475143 ?

#This keeps track of what the largest prime variable is
largestprime = 0
>>>>>>> Updates files from desktop

#this is our limiting fator that keeps track of the value we want the prime factors of 
number = 600851475143

<<<<<<< HEAD
#this keeps the value of the array to check against the highest
arrayval = 0

#this varialbe keeps track of the last highest prime (that way we have a way of catching it after it went over
secondhighest = 0

#this generates a list of the primes that we need credit to Wensheng Wang
def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]
#prebuilds the list of primes that we need for the program
prime = primes(100000000)
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
		print "the array val is hit"		
		highestprime = arrayval 
	#maintains the loop
	PC = PC + 1
	print arrayval
print largestprime
=======
#This keeps track of were we are in the loop factor loop
PC = 0

#keeps track of the number while we are in the prime loop
PC2 = 0

while PC <= number

	if number % PC == 0
		#Then it is a factor and we should check if it is prime
		


	#Resets PC2 and continues to count the progress through the loop
	PC2 = 0
	PC = PC + 1
>>>>>>> Updates files from desktop
