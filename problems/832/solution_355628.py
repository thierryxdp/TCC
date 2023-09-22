def eh_quadrada(matriz):
    if len(matriz) == len(matriz[0]):
        return True
    if len(matriz) != len(matriz[0]):
        return False
    if len(matriz) == 0:
        return True