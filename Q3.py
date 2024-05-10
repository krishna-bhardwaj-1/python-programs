a=[1,2,3,4,5]
max=a[0]
min=a[0]
for i in range(0,len(a)):
    if (max<a[i]):
        max=a[i]
    if(min>a[i]):
        min=a[i]

print(max,min)
        
        