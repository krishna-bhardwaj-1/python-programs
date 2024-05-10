a=[1,2,3,4]
odd=0
even=0
for i in range(0,len(a)):
    if (a[i]%2==0):
        even+=1
    else:
        odd+=1
if even>odd:
    print(even-odd)
else:
    print(odd-even)