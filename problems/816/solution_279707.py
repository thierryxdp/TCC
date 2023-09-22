def maiores(lista,n):
    L=lista
    L=lista+[n]
    F=L.sort()
    T=list.index(F,n)
    return F[T+1:]