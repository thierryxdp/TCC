def eh_quadrada(matriz):
    '''Checa se a matriz fornacida é quadrada;
       list -> bool'''
    if matriz == []:
        return True
    else:
        return len(matriz) == len(matriz[0])