def filtra_pares(t):
    """Tem como objetivo receber uma tupla de 4 elementos e 
    retornar uma nova tupla, apenas com os números pares
    tupla > tupla"""
    pares = tuple()
    for valor in t:
        if valor%2==0:
            pares.append(valor)
    return pares