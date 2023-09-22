def eh_quadrada(matriz):
    '''retorna true se uma dada matriz e quadrada ou false caso contrario; list -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif (len(matriz) == 0) and (len(matriz[0]) == 0):
        return True
    else:
        return False