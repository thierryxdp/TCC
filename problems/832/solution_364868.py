def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada, ou seja, vazia'''
    linha = len(matriz)
    if linha == 0:
        return True
    coluna = len(matriz[0])
    return linha == coluna