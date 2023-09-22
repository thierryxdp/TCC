def eh_quadrada(matriz):
    """identifica se a matriz dada é quadrada ou nao;
    list->bool"""
    if len(matriz) == 0 or len(matriz) == len(matriz[0]):
        return True
    else:
        return False