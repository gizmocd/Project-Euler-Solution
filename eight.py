# Project Euler, problem 8

target = open('eight_number.txt','r')

mystring = ''
my_input = target.read()
while(my_input != ''):
    mystring += my_input
    my_input = target.read()
target.close()

#print(mystring)

answer = 0
for i in range(0, len(mystring) - 13):
    temp = 1
    limit = 13
    j = 0
    while j < limit:
        if mystring[i + j] == '\n':
            limit += 1
        else:
            temp *= int(mystring[i + j])
        j += 1
    if temp > answer:
        answer = temp

print('####')
print(answer)
