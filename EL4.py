#Find the largest palindrome made with 2 3 digit numbers multiplied together

#The first triple digit number that we run through 
digit1 = 100

#The second tripple digit number that we run through
digit2 = 100

#the continuation variable to continue the program running
cont = 1

#The bigest palindrome that has been detected to date 
Palin = 0

#The palindrome number multiplied together
palinmulti = 0

#this is the value of the reversed number
palinreverse = 0


while cont == 1:
	#converts to single variable for easier use 
	palinmulti = digit1 * digit2
	
	#converts the palinmulti to a string so that we can flip it 
	palinmulti = str(palinmulti)

	#reverses the value in order to detect wether it was a palindrome
	palinreverse = palinmulti[::-1]
	
	#Checks if the number is a palindrome 
	if palinreverse == palinmulti:
		#then it is the new highest palindrome
		Palin = palinmulti

	###################### RUNS LOOP #########################
	
	#CAtches when seccond digit is about to go over	
	if digit2 == 999:
		#ends the run and returns the answer
		cont = 0	
	#the if catches when the first digit is about to go to 4 digits	
	if digit1 == 999:
		#Sets the second 3 digit number up one 
		digit1 = 100
		digit2 = digit2 + 1
	
	#The incrementation for the next run
	digit1 = digit1 + 1
#Return the answer
print Palin
