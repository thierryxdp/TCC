def eh_quadrada(matriz):
    '''Recebe uma matriz e retorna True se for quadrada e false se não for.
    matriz->bool'''
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False