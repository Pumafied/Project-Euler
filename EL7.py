#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

<<<<<<< HEAD
#this variable is where we will store what we use to display the number that we need
highprime = 0

#this is the number of the prime that we want
desiredprime = 100001

#keeps track of the programs place in the loop
PC = 0

#keeps track of the number of prime that we are on in the loop
prime = 0

#generates a list of prime numbers that is specified credit to  Wensheng Wang for the list generator
def primes(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

#stores a list big enough to have all of the data that we need
primelist = primes(10003)

#the loop that does the actual finding of the primes
while prime <= desiredprime:
	if PC in primelist:
		#then we advance the prime that we are on by one after we check to make sure that it isnt the final answer
		print PC
		print prime
		if prime == desiredprime:
			#we have found our answer and we make sure that it is in the variable that is printed out
			highprime = prime
		prime = prime + 1	

	#preforms the necessary maintance on the loop
	PC = PC + 1
#we return the 10001 prime that we find 
print highprime
input('End Of Program')
#freezes on number 1228 although I am reletivly confidant that it is right. to be checked on a faster computer.
=======
#Brute force prime checker

#The Desired prime number is the number of the prime number that we want.
DesiredPrime = 10002;
#The number that is being checked to see if is prime 	
PrimeChecked = 0;
#The number that we are on in the checking sequence
PrimeCounter = 0;

while PrimeCounter != DesiredPrime:
	#The number that is being used to loop through and attempt to find a multiple
	PrimeCheckVar = 5;
	while PrimeCheckVar <= PrimeChecked:		 	
		if PrimeCheckVar == PrimeChecked:
			#it is prime if this code ends up executing
			PrimeCounter = PrimeCounter + 1;
			if PrimeCounter == DesiredPrime:
				print PrimeChecked;
				break;
			break;
		elif PrimeChecked%PrimeCheckVar == 0: 
			#Then its not prime and we dont flag it and move on 	
			break;
		PrimeCheckVar = PrimeCheckVar + 1;
	#adds one to the guess to run through the loop again 
	PrimeChecked = PrimeChecked + 1;
>>>>>>> Updates files from desktop
