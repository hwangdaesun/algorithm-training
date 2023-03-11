import sys

while(1):
    s = input()
    b = True
    if(s == '0'):
        break
    if(len(s) == 1):
        print("yes")
    else:
        mid = len(s)//2
        for i in range(mid):
            if(s[i] != s[(len(s)-1) - i]):
                print("no")
                b = False
                break
            else:
                continue
        if(b):
            print("yes")
    

# 길이가 3이상이고 홀수 
 

# 아니면 no 출력