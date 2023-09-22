def eh_quadrada(matriz):
    if len(matriz) == len(matriz[0]):
        return True
    if not len(matriz) == len(matriz[0]):
        return False