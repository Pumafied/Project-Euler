#Find the largest palindrome made with 2 3 digit numbers multiplied together

#The first triple digit number that we run through 
pal1 = 100

#The second tripple digit number that we run through
pal2 = 100

#the continuation variable to continue the program running
cont = true

#The bigest palindrome that has been detected to date 
Palin = 0

#The palindrome number multiplied together
palinmulti = 0

#Used to keep track of wether the number that we just checked is a palindrome
ispal = no

while cont == true
	#converts to single variable for easier use 
	palinmulti = pal1 * Pal2
	
	#Checks if the number is a palindrome 


	#Checks if it is the largest palindrome 
	if ispal == true and palinmulti >= Palin:
		palin = palinmulti


	###################### RUNS LOOP #########################
	#the if catches when the pal1 is about to go to 4 digets
	if pal1 == 999
		#Sets the second 3 digit number up one 
		pal1 = 100
		pal2 = pal2 + 1
	#CAtches when pal2 is about to go over
	if pal2 == 999
		#ends the run and returns the answer
		cont = false
	#The incrementation for the next run
	pal1 = pal1 + 1
	ispal = no

#Return the answer
print Palin
