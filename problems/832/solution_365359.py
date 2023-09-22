def eh_quadrada(matriz):
    """identifica se uma matriz e quadrada. list -> bool"""
    if matriz == []:
        return True
    if len(matriz[0]) == len(matriz):
        return True
    else:
        return False