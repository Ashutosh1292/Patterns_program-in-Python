n=int(input(" enter no "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(end=" ")
    for j in range(1,n+2-i):
        print(i,end=" ")
    print(" ")