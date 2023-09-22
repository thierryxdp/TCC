def filtra_pares(lista):
    """filtra os números pares de uma lista"""
    pares = list()
    for x in lista:
        if x%2==0:
            pares.append(x)
    return pares