def eh_quadrada(matriz):
    """Para retornar se a matriz é quadrada, digite;
    matriz->bool"""
    if len(matriz) == 0:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False