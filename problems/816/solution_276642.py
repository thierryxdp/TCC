def maiores(lista, n):
    """..."""
    list.sort(lista)
    x = list.index(lista, n)
    nova_lista = lista[x:]
    
    return nova_lista