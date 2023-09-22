def eh_quadrada(matriz):
    """Funcao que identifica se uma matriz de entrada e
    quadrada, retornando True, ou nao, retornando False;
    list[list] -> bool"""
    if matriz==[] or len(matriz)==len(matriz[0]):
        return True
    else:
        return False