def eh_quadrada(matriz):
    '''função booleana que diz se uma matriz dada é quadrada ou não;
    list(list) -> bool'''
    if  matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False