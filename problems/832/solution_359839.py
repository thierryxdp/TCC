def eh_quadrada(matriz):
    if len(matriz) == 0:
        return True
    X = len(matriz)
    Y = len(matriz[0])
    if X != Y:
        return False 
    else:
        return True