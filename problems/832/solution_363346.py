def eh_quadrada(matriz):
    '''docs'''
    
    if matriz == list():
        return True
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False