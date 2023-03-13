s = input()

words = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count = 0


for i in range(len(words)):
    if words[i] in s:
        a = s.count(words[i])
        s = s.replace(words[i]," ")
        count += a

s=s.replace(" ","")
print(count + len(s))

