from collections import deque

n = int(input())

d = deque()

for i in range(n):
    a = input().split()
    d.append(a)


for i in range(n):
    count = 1
    for j in range(n):
        x1,y1 = d[i]
        x2,y2 = d[j]
        if(int(x1) < int(x2) and int(y1) < int(y2)):
            count += 1
    print(count, end = " ")