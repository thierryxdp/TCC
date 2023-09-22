def filtra_pares(t):
    """função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elemtnos pares da primeira tupla"""
    pares = list(filter(lambda x: x % 2 == 0, t))
    pares=tuple(pares)
    return pares