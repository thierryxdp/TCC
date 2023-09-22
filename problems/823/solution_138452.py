def faltante(l):
    if 1 not in l:
        return 1
    total = len(l)
    lista1 = range(1,total+1)
    if lista1==l:
        return l[-1]+1