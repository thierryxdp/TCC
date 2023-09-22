def filtra_pares(t):
    """recebe uma tupla com 4 elementos, e retorna uma nova tupla apenas com seus elementos pares;
    tuple -> tuple"""
    pares=list(filter(lambda x:x%2==0))
    pares=tuple(pares)
    return pares