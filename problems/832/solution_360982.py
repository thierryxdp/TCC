def eh_quadrada(matriz):
    """função que identifica se uma matriz é quadrada"""
    lin = len (matriz)
    if lin == 0:
        return True
    col = len(matriz[0])
    if lin == col:
        return True
    else:
        return False