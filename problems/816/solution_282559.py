def maiores(lista, n):
    """Retorna todos os números de uma lista maiores que n.
    Entrada: list, float
    Saída: list
    """
    list.sort(lista)
    o = n-1
    return lista[:o]