def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada ou não.
    list -> bool'''
    if len(matriz) == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False