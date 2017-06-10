#Project Euler, problem 1

i = 0
j = 0
mysum = 0
while i < 1000:
    mysum += i
    i += 3
while j < 1000:
    if(j % 3 != 0): #can't add same number twice
        mysum += j
    j += 5
print(mysum)
