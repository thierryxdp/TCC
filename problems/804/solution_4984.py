def filtra_pares(tupla1):
    """Devolve apenas os números pares de uma tupla"""
    tupla1 = []
    tupla2 = []
    for valor in tupla1:
        if valor//2 == 0:
            tupla2.append(valor)
            return tuple(tupla2)