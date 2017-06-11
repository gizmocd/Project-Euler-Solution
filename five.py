# Project Euler, problem 5

import three

mylist = []
lister = 0
for i in range(2,21):
    mylist.append([])
    mylist[lister] = three.factor(i)
    lister += 1

list_length = len(mylist)

for i in range(0, list_length): #in each list...
    for j in range(0, len(mylist[i])): #access each element ...
        for k in range(0, list_length): #in each list...
            #print("k equals " + str(k))
            #print(len(mylist[k]))
            for m in range(0, len(mylist[k])): #access each element ...
                if  mylist[i][j] != 1 and i != k and mylist[i][j] == mylist[k][m]:
                    mylist[i][j] = 1
#print(mylist)
answer = 1
for i in range(0, list_length): #in each list...
    for j in range(0, len(mylist[i])): #access each element ...
        answer *= mylist[i][j]

print(answer)
