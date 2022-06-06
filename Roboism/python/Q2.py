def func(creditNumber):
    l = len(creditNumber)
    for i in range(l-4,l):
        creditNumber[i] = '*'
    creditNumber = ''.join([str(i) for i in creditNumber])
    return creditNumber

creditNumber = list(input("Enter credit number: "))
newCreditNumber = func(creditNumber)
print(newCreditNumber) 