def maiores(L,n):
    if n in L:
        indice =list.index(L,n)
        n = L[indice]
        return L[indice:]