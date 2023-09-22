def eh_quadrada(matriz):
    '''Função booleana que identifique se uma matriz é quadrada.
       matriz ---> matriz'''
    if len(matriz) == range(len(matriz[0])):
        return True
    else:
        return False