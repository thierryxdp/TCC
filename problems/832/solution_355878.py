def eh_quadrada (matriz):
    '''
    A função informa se a matriz é
    quadrada ou não.
    list -> bool
    '''
    if matriz != [[]]:
        linhas = len(matriz)
        if linhas == len(matriz[0]):
            return True
        else:
            return False            
    else:
        return True