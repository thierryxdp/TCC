def maiores(lista, n):
    """Retorna todos os números de uma lista maiores que n.
    Entrada: list, float
    Saída: list
    """
    novalista = list.sort(lista)
    o = n+2
    return novalista[o:]