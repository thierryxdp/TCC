def eh_quadrada(matriz):
    """identifica se a matriz dada é quadrada ou nao"""
    """list->bool"""
    if len(matriz) == len(matriz[0]) or matriz == []:
        return True
    else:
        return False