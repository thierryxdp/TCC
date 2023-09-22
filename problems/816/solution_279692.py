def maiores(lista,n):
    L=lista
    L=lista+list([n])
    L=list.sort(L)
    t=list.index(L,n)
    return L[t+1:]