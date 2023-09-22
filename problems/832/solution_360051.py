def eh_quadrada(matriz):
    """identifica se a matriz dada é quadrada ou nao"""
    """list->bool"""
    numL = len(matriz)
    numC = len(matriz[0])
    if numL == numC:
        return True
    else:
        return False