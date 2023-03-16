n = int(input())

list = []

while(n>10):
    list.append(n%10)
    n //= 10
list.append(n)

list.sort(reverse=True)

for i in range(len(list)):
    print(list[i], end ="")
