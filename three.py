# Project Euler, problem 3

# 600851475143 - largest prime factor?

def isPrime(x):
    prime = True
    count = 3
    if x % 2 == 0:
        prime = False
        return prime
    else:
        while count < x:
            if x % count == 0:
                return False
            count += 2
    return prime

def factor(x):
    mylist = []
    while_bool = True
    i = 2 #iterator
    limit = round(x/2)
    if x == 1:
        return mylist
    while while_bool and i < limit:
        if x % i == 0:
            while_bool = False #stop looping!
            x = int(x/i)
            if not isPrime(i):
                mylist += factor(i)
            else:
                mylist += [i]
            mylist += factor(x)
        else:
            i += 1
    if while_bool:   #if x wasn't divisible...
        mylist += [x]
    return mylist

#print("#########")
print(max(factor(600851475143)))
print(max(factor(13195)))
