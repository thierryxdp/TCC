def eh_quadrada(matriz):
    ''' função booleana para identificar se uma matriz é quadrada;
    matriz-> bool'''
    for i in matriz:
        if len(matriz)==len(matriz[0]):
            return True 
        else: 
            return False