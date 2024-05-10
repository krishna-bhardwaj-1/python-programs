num=int(input("Enter a number to find the factorial: "))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print(fact)