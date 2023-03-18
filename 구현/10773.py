n = int(input())

answer = []

for i in range(n):
    a = int(input())
    if a == 0:
        del answer[-1]
    else:
        answer.append(a)

print(sum(answer))