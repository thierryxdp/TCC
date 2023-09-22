def eh_quadrada(matriz):
    """A Funcao verifica se a matriz e quadrada; list->bool"""
    primlista=len(matriz)
    if len(matriz) == 0:
        return True
    elif len(matriz[0]) == len(matriz):
        return True
    else:
        return False