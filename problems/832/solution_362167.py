def eh_quadrada(matriz):
    ''' identificação de uma matriz quadrada '''
    if len(matriz)>0:
        return len(matriz)==len(matriz[0])
    else:
        return true