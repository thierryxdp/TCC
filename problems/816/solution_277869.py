def maiores(L,n):
    indice=list.index(L,n)
    list.sort(L)
    return L[indice+1:]