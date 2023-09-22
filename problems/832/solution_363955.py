def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada; entrada->matriz;
    list(matriz)->bool'''
    lin= len(matriz)
    col=len(matriz[0])
    if lin == col:
        return True
    elif matriz == []:
        return False
    else:
        return False