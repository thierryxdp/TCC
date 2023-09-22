def eh_quadrada(matriz):
    '''função que determina se a matriz colocada como entrada é quadrada
       list -> bool'''
    if len(matriz)==len(matriz[0]):
        return bool(1)
    else:
        return bool(0)