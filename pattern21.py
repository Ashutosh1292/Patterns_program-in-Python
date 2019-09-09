n=int(input("enter "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(n+1-i,end=" ")
    print(" ")