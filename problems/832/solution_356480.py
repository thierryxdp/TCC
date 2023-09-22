def eh_quadrada(matriz):
    '''função booleana que identifica se uma matriz é quadrada, bool->bool'''
    linha=len(matriz)
    coluna=len(matriz[0])
    if matriz == [] or linha == coluna:
        return True
    else:
        return False