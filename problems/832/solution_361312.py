def eh_quadrada(matriz):
    '''Funçao que identifica se a matriz é quadrada ou não.'''
    '''list(list)->bool'''
    if matriz == []:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False