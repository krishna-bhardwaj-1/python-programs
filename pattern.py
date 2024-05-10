for x in range(0,5):
    for y in range(0,2*x-1):
        if (y % 2==0):
            print("\'",end="")
        else:
            print("\"",end="")
    print("")