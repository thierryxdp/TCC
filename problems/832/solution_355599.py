def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada'''
    if len(matriz)==0:
        return True
    elif len(matriz)!=len(matriz[0]):
        return False
    else:
        return True