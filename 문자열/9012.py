# ()가 있는 지 확인하고 있으면 지워버림 -> 반복
# 없다 -> 길이가 0이다 print(Yes) 길이가 0보다 크다? 그러면, print(no)

n = int(input())
for i in range(n):
    s = input()
    while ('()' in s):
        s =s.replace('()','')
    if(len(s) == 0):
        print("YES")
    else:
        print("NO")