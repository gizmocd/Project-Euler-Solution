# Project Euler, problem 4

def isPalindrome(x):
    x = str(x)
    length = len(x) - 1 # minus one -> zero indexed
    j = length
    for i in range(0, int(length/2) + 1):
        if x[i] != x[j]:
            return False
        else:
            j -= 1
    return True

def isThreeDigitDivisible(x):
    for i in range(100,1000):
        if x % i == 0 and len(str(int(x/i))) == 3:
            return True
    return False

start = 100**2
end = 999**2 #998001
answer = 0
for i in range(start,end + 1):
    if isPalindrome(i) and isThreeDigitDivisible(i):
        answer = i

print(answer)
