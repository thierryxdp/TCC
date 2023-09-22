def eh_quadrada(matriz):
    '''Funcao que identifica se uma matriz e quadrada
    list(list) -> bool'''
    linha = len(matriz)
    if matriz==[]:
        return True
    elif linha == len(matriz[0]):
        return True
    else:
        return False