s = input()

#MISSISSIPI
s = s.upper()

# 중복 제거 MISP
ss = list(set(s))

# 각 문자가 몇개씩 들어있는 지 -> 리스트
sslist = []
for i in ss:
    sslist.append(s.count(i))

# 개수 리스트에서 최대를 구한다.
# 최대가 중복되있는 지 확인하고, 중복 됬다면, ?출력 중복이 아니라면 해당 인덱스의 값 출력

a = max(sslist)
if(sslist.count(a)>1):
    print("?")
else:
    print(ss[sslist.index(a)])