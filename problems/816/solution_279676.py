def maiores(lista,n):
    """retorna uma nova lista com numeros maiores que n da lista orginal"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]