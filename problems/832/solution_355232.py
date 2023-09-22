def eh_quadrada(matriz):
    '''testa se matriz dada eh quadrada ou eh vazia
    list->bool'''
    if len(matriz) == 0:
        return True
    else:
        return len(matriz)==len(matriz[0])