def eh_quadrada(matriz):
    """
    Ao inserir uma matriz, se ela for quadrada retornará true,
    e retornará false se não for
    list-> bool
    """
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False