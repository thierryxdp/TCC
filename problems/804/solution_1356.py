def filtra_pares(lista):
    """filtra os elementos pares de uma lista"""
    return filter(lambda x: x % 2 == 0, list(lista))