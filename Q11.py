x=(1,2,3,4)
y=(4,5,6,7)
c=[]
A1=list(x)
A2=list(y)
for i in range(0,len(A1)):
    c.append(A1[i]+A2[i])
print(tuple(c))