def filtra_pares (tupla):
    """
    funcao que recebe uma tupla com 4 elem.
    retorna uma nova tupla contendo apenas elem pares
    da tupla original
    tuple -> tuple
    """
    pares = tuple(filter(lambda x: x%2==0, tupla))
    return pares