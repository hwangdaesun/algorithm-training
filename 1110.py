n = int(input())

count = 0
origin = n
while(1):
    if(n<10):
        # 07 -> 7 ->77
        n = n*10 + n
    else:
        # 1의자리
        # 26 -> 6
        a = n % 10
        # 10의자리
        # 26 -> 2
        b = n // 10
        c = a*10 + ((a+b)%10)
        n = c
    count+=1
    if(origin == n):
        print(count)
        break



