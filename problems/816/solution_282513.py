def maiores(lista, n):
    """Retorna uma lista com os elementos maiores que n na lista dada como entrdada.
list, int -> list"""
    list.insert(lista,0,n)
    list.sort(lista)
    p = list.index(lista,n)
    r = lista[p+1:]
    return r