def maiores(lista, n):
    """Retorna uma lista com os elementos maiores que n na lista dada como entrdada.
list, int -> list"""
    list.insert(lista,0,n)
    list.sort(lista,reverse=True)
    p = list.index(lista,n)
    r = lista[0:p]
    return r