n = int(input())

gaesu5 = n // 5 + 1

answer = []
# 0~3
for i in range(gaesu5):
    if str((n - (i * 5)) / 3).split('.')[1] == '0':
        gaesu3 = (n - (i * 5)) / 3
        gaesu3 = int(gaesu3)
        sum = i + gaesu3
        answer.append(sum)
    else:
        continue
if(len(answer) == 0):
    print(-1)
else:
    print(min(answer))

# gaesu3  * 3 + gaesu5 * 5 == n
# gaesu3 + gaesu5 == 최소
