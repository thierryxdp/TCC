def maiores(lista,n):
    L=lista
    list.append(L,n)
    list.sort(L)
    indece=list.index(L,n)
    z=indece+1
    L=L[z:]
    return L