noSelfL = []

def sol(n):
    sum = 0
    while(n>0):
        sum+=n%10
        n = n // 10
    return sum

for i in range(10000):
    num = i+1
    aa = sol(num)
    noSelf = num + aa
    noSelfL.append(noSelf)


for j in range(1,10000):
    if j not in noSelfL:
        print(j)



