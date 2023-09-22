def eh_quadrada(matriz):
    """Determina se uma matriz é ou não uma matriz quadrada
       lista ~> bool"""
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False