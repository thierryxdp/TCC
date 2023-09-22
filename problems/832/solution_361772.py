def eh_quadrada(matriz):
    """Identifica se uma matriz é quadrada ou não;
    list -> bool"""
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False