def maiores(L,n):
    if n in L:
        indice=list.index(L,n)
        list.sort(L)
        return L[indice+1:]
    if n not in L:
        return L