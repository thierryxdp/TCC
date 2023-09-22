def maiores(lista, n):
    l1=list.insert(lista,0, n)
    l2=list.sort(l1)
    i=list.index(l2, n)
    return l2[2:]