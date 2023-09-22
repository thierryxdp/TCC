def maiores(lista,listan):
    """retorna uma nova lista com numeros maiores que n da lista orginal"""
    lista.sort()
    return listan(lista[-1])