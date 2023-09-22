def eh_quadrada(matriz):
    '''descrição'''
    if len(matriz)==0:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False