def eh_quadrada(matriz):
    '''Observa se a matriz é quadrada ou não
    mat->bool'''
    lin=len(matriz)
    if lin==0:
        return True
    col=len(matriz[0])
    if lin==col:
        return True
    else:
        return False