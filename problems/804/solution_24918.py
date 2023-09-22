def filtra_pares(valores):
    y = []
    for x in valores:
        if x%2 == 0:
            y.append(x)         
    return tuple(y)