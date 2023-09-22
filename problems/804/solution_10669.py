def filtra_pares (tupla):
    """Retorna uma nova tupla apenas contendo apenas os elementos pares da tupla
    original na mesma ordem em que se encontravam: tuple -> tuple"""
    return [ n for n in tupla if n % 2 == 0 ]