def eh_quadrada(matriz):
    """
    """
    if matriz == []:
        return True
    elif type(matriz[0]) == list:
        return len(matriz) == len(matriz[0])