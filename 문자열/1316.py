n = int(input())
groupsu = 0

for i in range(n):
    word = input()
    wordset = set(word)
    isOkay = True
    for i in wordset:
        gaesu = word.count(i)
        if(gaesu == 1):
            continue
        else:
            if(i*gaesu in word):
                continue
            else:
                isOkay = False
                break
    if(isOkay):
        groupsu += 1
print(groupsu)


# 일단은 중복을 없앤다. -> hapy
# h가 s에 몇개있는 지 확인 -> 1개라면 괜찮, 2개이상이라면 확인들어감
# 2개이상일 때,'p'*count가 있는 지 확인 있으면 괜찮 없으면 안되

