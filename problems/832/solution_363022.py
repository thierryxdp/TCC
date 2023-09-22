def eh_quadrada(matriz:list)->bool:
    """ identifica se uma matriz é quadrada ou nao"""
    for i in matriz:
        if len(matriz)!=len(matriz[0]):
            return False
    return True