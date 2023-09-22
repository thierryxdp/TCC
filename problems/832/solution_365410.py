def eh_quadrada(matriz):
    '''retorna true se uma dada matriz e quadrada ou false caso contrario; list -> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False