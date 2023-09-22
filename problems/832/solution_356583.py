def eh_quadrada(matriz):
    '''Função que verifica se a matriz é quadrada'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False