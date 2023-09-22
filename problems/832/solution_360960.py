def eh_quadrada(matriz):
    '''retorna se a matriz é quadrada ou não; list->bool'''
    lin=len(matriz)
    col=len(matriz[0])
    return lin==col