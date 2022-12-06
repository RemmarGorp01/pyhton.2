n=int(input("Enter a number:\n"))
for i in range(2,n+1):
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
    print()
    
