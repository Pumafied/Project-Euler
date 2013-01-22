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
