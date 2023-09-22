def eh_quadrada(matriz):
    '''função booleana que diz se uma matriz dada é quadrada ou não;
    list(list) -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == [[]]:
        return True
    else:
        return False