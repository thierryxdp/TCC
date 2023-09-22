def eh_quadrada(matriz):
    '''Dado uma matriz, retorna True caso seja quadrada e False caso contrario.
    list -> bool'''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else: 
        return False