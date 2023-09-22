def eh_quadrada(matriz):
    '''
    função booleana que identifica se uma matriz é quadrada.
    '''
    
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False