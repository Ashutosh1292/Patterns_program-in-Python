n=int(input("enter "))
for i in range(1,n+1):
    for j in range(1,i+1,2):
        print("*",end=" ")
    print(" ")