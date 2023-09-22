def eh_quadrada(matriz):
    if matriz == []:
        return True
    if len(matriz[0]) == len(matriz):
        return True
    else:
        return False