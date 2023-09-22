def maiores(lista,n):
    """função que retorna uma lista somente com os números maiores que n
    list, int -> list"""
    list = lista
    list.append(n)
    list.sort()
    list = list[(list.index(n) + 1):]
    return list