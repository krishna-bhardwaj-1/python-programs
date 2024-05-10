for i in range(1,6):
    c=1
    for j in range(1,i+1):
        print(c,end=" ")
        c=c*(i-j)//j
    print()