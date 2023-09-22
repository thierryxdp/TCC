def maiores(lista, n):
    """Retorna todos os números de uma lista maiores que n.
    Entrada: list, float
    Saída: list
    """
    lista2 = list.sort(lista)
    o = n+2
    return lista2[o:]