s="python"
a=[]
for i in range(0,len(s)):
    a.append(s[i])
for i in range(0,len(a),2):
    a[i],a[i+1]=a[i+1],a[i]
c="ab"

reversed(c)
print(c)
