def eh_quadrada(matriz):
    '''Essa função identifica se uma função é quadrada ou não.
    list >>> bool '''
    
    if matriz == list():
        return True
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False