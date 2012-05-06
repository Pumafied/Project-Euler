#Power to the power generator

#Power variable
Power = 1

#Power Limiter 
PowerLimit = 1000

#Power Sum runner
PowerSum = 0

while Power <= PowerLimit:
	#Add the sum 
	PowerSum = (Power ** Power) + PowerSum
	Power =	Power + 1
PowerSumInt = str(PowerSum)


FinalAnswer = PowerSumInt[-11:] 

print FinalAnswer 
input('End Of Program')