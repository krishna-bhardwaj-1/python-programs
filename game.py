s=input()
c=0
d=0
for i in range(0,len(s)):
    if s[i]=='C':
        c=c+1
    if s[i]=='I':
        d=d+1
    if d>2:
        break
if(d<3):
    print("You won")
    print(c)
else:
    print("Game over")
    print(c)