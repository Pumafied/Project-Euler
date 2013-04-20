#Find the largest palindrome made with 2 3 digit numbers multiplied together
#product made

currentMax = 0

for left in range(1,1000):
    for right in range(1,1000):
        current = left * right
        currentRev = str(current)[::-1]
        if current == int(currentRev) and  current > currentMax:
            currentMax = current
print currentMax
