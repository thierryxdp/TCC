def faltante(l):
    count = 0
    if 1 not in l:
        return 1
    total = len(l)
    lista1 = range(1,total+1)
    if lista1==l:
        return l[-1]+1
    for i in l:
        if i+1 != l[count+1]:
            return i+1
        count = count + 1