def maiores(lista,n):
    L=lista
    L=lista+[n]
    F=L.sort()
    T=F.index(n)
    return T