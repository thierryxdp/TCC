def maiores(lista,n):
    """."""
    lista[0:0] = [n]
    list.sort(lista)
    x = list.index(lista,n)
    return lista[x+1:]