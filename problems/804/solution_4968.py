def filtra_pares(x):
    """Devolve apenas os números pares de uma tupla"""
    lista1 = ([*x])
    lista2 = ([])
    for valor in lista1:
        if valor%2 == 0:
            return (lista2)