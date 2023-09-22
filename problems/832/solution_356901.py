def eh_quadrada(matriz):
    ''' identifica se a matriz de entrada e quadrada ou nao. lista->bool'''
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False