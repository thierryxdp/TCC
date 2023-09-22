def maiores(lista,n):
    L=lista
    L=lista+[n]
    F=L.sort()
    T=F.index(n)
    return F[T+1:]