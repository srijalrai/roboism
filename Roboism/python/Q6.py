x=int(input("enter lower limit: "))
y=int(input("enter upper limit: "))
for i in range(x,y+1,1):
    p=0
    for j in range(2,i):
        if(i%j==0):
            p=p+1
    if(p==0):
        print(i)
     