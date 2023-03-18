n,m = map(int,input().split())

a = set()

for i in range(n):
    a.add(input())

b = set()

for j in range(m):
    b.add(input())

c = list(a & b)
c.sort()

print(len(c))
for i in range(len(c)):
    print(c[i])