def eh_quadrada(matriz):
    """Identifica se a matriz dada como entrada e quadrada ou nao;
    list -> Bool
    """
    if matriz == list():
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False