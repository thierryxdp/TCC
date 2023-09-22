def maiores(lista,n):
    L=lista
    L=lista+[n]
    F=L.sort()
    T=list.index(L,n)
    return T