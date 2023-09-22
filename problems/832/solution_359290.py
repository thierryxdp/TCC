def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    for elemento in matriz:
        if elemento:
            return False
    return True