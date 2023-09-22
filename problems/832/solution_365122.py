def eh_quadrada(matriz):
    """funcao booleana para identificar se uma matriz e quadrada
    list -> bool"""
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False