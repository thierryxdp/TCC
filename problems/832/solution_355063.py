def eh_quadrada(matriz):
    '''eh_quadrada recebe uma matriz e devolve se a matriz e quadrada ou não.
    matriz-->bool.'''
    if matriz==[] or len(matriz)==len(matriz[0]):
        return 0==0
    else:
        return 0!=0