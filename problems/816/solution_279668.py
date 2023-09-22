def maior_elemento(lista):
    """retorna uma nova lista com numeros maiores que n da lista orginal"""
    lista.sort()
    return lista[-1]