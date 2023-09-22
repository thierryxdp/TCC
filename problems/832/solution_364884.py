def eh_quadrada(matriz):
    '''função booleana que dada uma matriz, verifica se
    ela é quadrada;
    matriz-> bool'''
    if matriz==[]:
        return True
    for i in range(len(matriz)):
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False