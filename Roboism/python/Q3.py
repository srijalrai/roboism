def calc(i,s,j):
    if(s=='+'):
        return i+j
    if(s=='-'):
        return i-j
    if(s=='*'):
        return i*j
    if(s=='/'):
        return i/j
i=int(input("enter first parameter: "))
s=input(("enter second parameter: "))
j=int(input(("enter third parameter: ")))
print(calc(i,s,j))