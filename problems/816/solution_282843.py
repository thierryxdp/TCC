def maiores(lista, n):
    l1=list.insert(lista,0, n)
    list.sort(l1)
    i=list.index(l1, n)
    return l1[i:]