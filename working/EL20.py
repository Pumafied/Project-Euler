# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of digits in !100
factor = 10
i = factor
currentFact = 1
factSum = 0
while i > 0:
    currentFact = currentFact * i
    factor -= 1
    print currentFact
print factSum
