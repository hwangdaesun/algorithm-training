# 이진탐색 시간초과.. why??
from bisect import bisect_left

n,m = map(int,input().split())
words = list(input() for _ in range(n+m))

lst = words[n:m+m]
lst.sort()
answers = []

for i in range(0,n):
    if words[i] in lst:
        answers.append(lst[bisect_left(lst,words[i])])

answers.sort()
print(len(answers))
for i in range(len(answers)):
    print(answers[i])

