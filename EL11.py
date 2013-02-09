#What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 2020 grid?

#first we store the above numbers in a 3D array

#we create a variable for the vertical products highest vertically
MaxVertical = 0

#we create a variable that checks the products horizontally
MaxHorizon = 0

#we create a variable that checks all of the products that slant to the top to bottom left to right
MaxTop = 0

#we create a variable that checks all of the products that slant the oppisite of the way above
MaxBottom = 0 

#create a variable to be used to keep track of the highest total of the four 
highestproduct = 0 

#creates a variable  set that is the top value of the chain (the basis for the other 3 numbers)
topnumx = 0

topnumy = 0

#this is the value of the first number in the chain

#this is the value of the seccond number in the chain

#this is the value of the third number in the chain 

#this is the value of the fourth number of the chain

#this is the maximum xcoordinate that the array has starting in the top left corner with the value of 1
xmax = 20

#this is the maximum y coordinate that the array can have starting at the top with the value 1

ymax = 20

#creates a test variable that is used for testing the products against the current max
curmax = 0

#the first array checks all of the vertical products
#uses the two variables to get the index location and then the value for the second. continues on like this
#then multiplies together to see if it is the highest value and if it is then it changes the highest value to the product
#loops over the first row 
#then moves the y value one down
#once it hits the  bottom right then it stops
while 

 
#the seccond array checks all of the horizontal products

#resets the curent maximum variable so that it is clear for the next loop
curmax = 0

#this third array checks all of the diagonal letters that slant to the top to bottom left to right 

#resets the curent maximum variable so that it is clear for the next loop
curmax = 0

#this forth array checks all the the numbers that slant the oppisite of the way above

#resets the curent maximum variable so that it is clear for the next loop
curmax = 0


#we then compare to see which of the four loops has returned the highest numbers

#we print out the number that is the greatest product available
print highestproduct
