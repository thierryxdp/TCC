def eh_quadrada(matriz):
    '''retorna se a matriz é quadrada ou não; list->bool'''
    lin=len(matriz)
    if lin>0:
        col=len(matriz[0])
    return lin==col