#calculates the sum of all primes beneath 2 million

#initializes the program counter
PC = 0

#lists the number that we want to go up to 
top = 2000000

#used to figure out if the number is prime or not
isprime = 0

#this keeps track of the sum of the primes to date
primesum = 0

#generates an array of all of the primes that we need
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
#this number generates the first twomillion primes guranteeing that we will have them high enough
primes(2000000)


while PC <= top:
	#this loop finds out if the number that we are testing is prime	
	while isprime <= PC:
		if isprime == PC: 
			primesum = primesum + PC
		#preforms maintanince on the top loop
		isprime = isprime + 1
	#preforms maintinance on the loop
	PC = PC + 1
	isprime = 0
print primesum
#this keeps the terminal open for all of you windows users
fin = input("End of Program!")
