def func(lst, flag):
    if flag=='asc':
        lst.sort()
        return lst
    elif flag=='desc': 
        lst.sort(reverse=True)
        return lst
    else: 
        return lst
lst = [int(num) for num in input().split()]
flag = input("asc, desc or none: ")
lst = func(lst, flag)
print(lst)
    