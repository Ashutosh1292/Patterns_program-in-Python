n=int(input("rangr "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    for j in range(1,i+1):
        print(end=" ")
    print(" ")