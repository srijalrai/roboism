s=input('enter string: ')
s1='123456789'
l=[]
for i in s:
    for j in s1:
        if(i==j):
            l.append(eval(i))
x=0
for i in l:
    x=x+i
print(x)