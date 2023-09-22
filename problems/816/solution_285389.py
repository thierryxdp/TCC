def maiores(lista,n):
    L=lista
    L=list.append(L,n)
    L=list.sort(L)
    I=list.inde(L,n)
    return L[0:I]