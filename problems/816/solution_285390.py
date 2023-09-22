def maiores(lista,n):
    L=lista
    L=list.append(L,n)
    lista_orde=list.sort(L)
    indece=list.index(L,n)
    L=[0:indece]
    return L