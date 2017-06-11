# Project Euler, problem 6

summ = 0
square_sums = 0
for i in range(1, 101):
    summ += i
    square_sums += i**2

print(summ**2 - square_sums)
