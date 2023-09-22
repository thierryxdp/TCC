def maiores(lista,lista2):
    """retorna uma nova lista com numeros maiores que n da lista orginal"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]