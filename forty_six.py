import math

def isPrime(x):
    count = 5
    if x % 2 == 0 or x % 3 == 0:
        return False
    elif (x-1) % 6 != 0 and (x+1) % 6 != 0:
        return False
    else:
        while count <= int(x/2):
            if x % count == 0:
                return False
            count += 2
    return True

def listLowerPrimes(x):
    # assume number greater than 17
    primelist = [2,3]
    i = 6
    while i < x:
        if isPrime(i-1):
            primelist += [i-1]
        if isPrime(i+1):
            primelist += [i+1]
        i += 6
    return primelist

#mylist = listLowerPrimes(80)

for i in range(4, 36000):
    if i % 2 != 0 and not isPrime(i):
        temp_list = listLowerPrimes(i)
        #print(temp_list)
        boole = True
        for j in range(0,len(temp_list)):
            temp = 0
            count = 1
            while temp < i and boole == True:
                temp = temp_list[j] + 2 * (count**2)
                if temp == i:
                    boole = False
                else:
                    count += 1
        if boole == True:
            print(i)



        
