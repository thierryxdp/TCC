def eh_quadrada(matriz):
    ''' função booleana para identificar se uma matriz é quadrada;
    matriz-> bool'''
    for i in range (len(matriz)):
        if len(matriz)==len(matriz[0]) and matriz==[]:
            return True 
        else: 
            return False