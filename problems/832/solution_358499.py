def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada ou nao
    entra:lista
    sai:booleano'''
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False