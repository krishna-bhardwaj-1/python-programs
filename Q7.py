a=[1,2,3,4,5]
odd=[]
even=[]
for i in range(0,len(a)):
    if (a[i]%2==0):
        odd.append(a[i])
    else:
        even.append(a[i])
    
print(even)
print(odd)