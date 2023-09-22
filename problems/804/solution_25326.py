def filtra_pares(x):
    nmrs = [x]
    pares = []
    for valor in nmrs:
        if valor % 2 == 0:
            pares.append(valor)
            return pares