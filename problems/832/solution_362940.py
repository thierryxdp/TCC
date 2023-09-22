def eh_quadrada(matriz):
    ''' Dada uma matriz, retorna se a matriz
    é quadrada ou não.
    list -> bool'''
    if len(matriz) == 0:
        return True
    lin = len(matriz)
    col = len(matriz[0])
    if lin == col:
        return True
    else:
        return False