def maiores(lista_nume_inteiros,n):
    L=lista_nume_inteiros
    list.insert(L,2,n)
    L.sort()
    k=list.index(L, n)
    return L[k+1: ]