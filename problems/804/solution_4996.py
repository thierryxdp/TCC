def filtra_pares(a, b, c, d):
    """Devolve apenas os números pares de uma tupla"""
    [a,b,c,d] = (tupla1)
    tupla2 = ([])
    for valor in tupla1:
        if valor % 2 == 0:
            tupla2.append(valor)
            return (tupla2)