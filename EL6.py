#find the difrence between the first 100 natural numbers and the square of the some
NaturalCounter = 1 
#natural number that we want to go up to 
NaturalNumber = 100
#number that we add to to check the sum 
NaturalSum = 0

#sums the number squared and then added
NaturalSum2 = 0

#Enter the loop and figure out the sum of all the natural numbers added first then squarded is 

while NaturalCounter <= NaturalNumber:

	#finds the sum of all of the numbers added first
	NaturalSum = NaturalCounter + NaturalSum
	
	# the counter by one then re loop
	NaturalCounter = NaturalCounter + 1 

SecondaryAnswer = NaturalSum ** 2
#reset the natural counter back down to 1 
NaturalCounter = 1
#counts the number  of squared first then adds them
while NaturalCounter <= NaturalNumber:
 	NaturalSum2 = NaturalCounter ** 2 + NaturalSum2
 	#add one and then reset the loop
 	NaturalCounter = NaturalCounter + 1

#Calculate the final answer of the loops 
FinalAnswer = SecondaryAnswer - NaturalSum2
#print out the final answer

print FinalAnswer
raw_input("End of Program")
