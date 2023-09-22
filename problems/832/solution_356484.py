def eh_quadrada(matriz):
    '''função booleana que identifica se uma matriz é quadrada, bool->bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha(matriz) == linha(coluna[0]):
        return True
    return False