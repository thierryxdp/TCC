def eh_quadrada(matriz):
    """vê se a raiz é quadrada."""
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    return False