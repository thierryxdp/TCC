def maiores(lista,n):
    L=lista
    list.append(L,n)
    list.sort(L)
    indece=list.index(L,n)
    y=L[indece:]
    M=list.remove(y,n)
    return M