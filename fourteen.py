#Project Euler problem 14

max_seq = 0
max_x = 0

for x in range(2,1000001):
    temp = int(x);
    seq = 0;
    while temp != 1:
        if temp % 2 == 0:
            temp = temp / 2;
        else:
            temp = 3*temp + 1;
        seq += 1;
    if seq > max_seq:
        max_seq = int(seq);
        max_x = int(x);

print(max_x);
