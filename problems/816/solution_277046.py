def maiores(L,n):
    """Retorna uma lista, que contenha todos os números da lista (L) maiores que n.
    lista,float-->lista)"""
    list.append(L,n)
    list.sort(L)
    x=list.index(L,n)
    return L[x+1:]