#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

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
