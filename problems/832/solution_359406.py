def eh_quadrada(matriz):
    '''avalia e retorna se uma matriz é ou não quadrada
    list-> bool'''
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False