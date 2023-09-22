def eh_quadrada(matriz):
    if matriz == []:
        return True
    elif len(matriz[0]) == len(matriz):
        return True
    else:
        return False