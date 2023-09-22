def ehquadrada(matriz):
    '''returna True se a matriz é quadrada
    list -> bool'''
    if len(matriz)!=0:
        return len(matriz)==len(matriz[0])