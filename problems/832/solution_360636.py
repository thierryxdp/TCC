def eh_quadrada(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    if lin == 0:
        return True
    elif lin == col:
        return True
    else:
        return False