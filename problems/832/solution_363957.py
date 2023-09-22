def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada; entrada->matriz;
    list(matriz)->bool'''
    matriz = matriz
    lin= len(matriz)
    col=len(matriz[0])
    if lin == col:
        return True
    elif matriz == []:
        return True
    else:
        return False