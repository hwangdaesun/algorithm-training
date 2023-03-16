n = int(input())

ss = []

for i in range(n):
    s = input()
    ss.append(s)

ss = list(set(ss))
ss.sort()

for a in range(len(ss)):
    for b in range(a+1,len(ss)):
        if(len(ss[a]) > len(ss[b])):
            ss[a], ss[b] = ss[b], ss[a]
       

for i in range(len(ss)):
    print(ss[i])

