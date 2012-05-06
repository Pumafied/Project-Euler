#Finds the smallest positive number that is evently divisible by all the numbers from 1-20

#The number that will be the lowest runners
Lowest = 0

#This varriable tracks the 1-20 numbers
track = 1

#runs the numbers up
runner = 20

#Tracks weather the value is still valid 
Valid = 1

#this tracks wether the loop needs to continue
end = 0

#loops over the numbers and check that they are evenly divisible by all of the numbers 1-20
while end ==  0:
	Valid = 1
	track = 1
	while Valid == 1 and track <=20:
		#This section checks an individual numbers validity 
		if track == 20:
                        #This exits the loop as we have found our answer
			Lowest = runner
			Valid = 0
			end = 1
			print Lowest
		elif runner % track == 0:
			Valid = 1
			#This flags the number valid
		elif runner % track != 0:
			Valid = 0
			#This flags the number valid and moves to the next number sequence
		track = track + 1 
	runner = runner + 1
	#increases the runner variable by one

#Returns the lowest possible
print "Lowest is"
print Lowest
print "End of Program"
        
