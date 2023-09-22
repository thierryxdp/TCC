def maiores (lista,n):
    """numeros inteiros e retorna uma lista
    list.int->list"""
    list = lista
    list.append(n)
    list.sort()
    list = list[(list.index(n)+1):]
    return list