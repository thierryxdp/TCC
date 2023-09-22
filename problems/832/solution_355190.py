def eh_quadrada(matriz):
    '''eh_quadrada recebe uma matriz e devolve se a matriz é quadrada com True ou não é quadrada com False.
    Assume que uma matriz vazia é considerada quadrada.
    list-->bool'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False