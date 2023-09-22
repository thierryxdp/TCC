def eh_quadrada(matriz):
    """Fumção que recebe uma matriz, retornando se essa matriz é quadrada ou não
    entrada: list(list)
    retorno: bool"""
    nlin= len(matriz)
    ncolun= len(matriz[0])
    if matriz is None:
        return True
    else:
        if len(matriz) == len(matriz[0]):
            return True
    return False