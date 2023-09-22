def eh_quadrada(matriz:list)->bool:
    '''Função booleana que identifica se uma matriz é quadrada.'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False