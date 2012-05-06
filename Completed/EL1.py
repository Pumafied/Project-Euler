#A simple script that adds up the numbers that are divisble by 3 or 5 

#keeps track of the sum
sums = 0

#keeps track of the programs place 
PC = 0

while PC < 1000:
	if PC % 5 == 0:
		#adds up the the modulous 5 and modulous 3 
		sums = PC + sums 
	elif PC % 3 == 0:
                #adds up the the modulous 5 and modulous 3 
		sums = PC + sums
	#counts the program up
	PC = PC + 1
#returns the answer
print sums
#off by 1000 
