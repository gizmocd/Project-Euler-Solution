# Project Euler, problem 2

fib = [1,2]
evensum = 2
while fib[1] < 4000000:
    temp = fib[1]
    fib[1] = fib[0] + fib[1]
    fib[0] = temp
    if fib[1] % 2 == 0:
        evensum += fib[1]
    #if fib[1] < 50: #debug
    #  print(str(fib[0]) + "," + str(fib[1])) #debug
print(evensum)
