def eh_quadrada(matriz):
    '''função que determina se a matriz colocada como entrada é quadrada
       list -> bool'''
    i=0
    while i<=len(matriz):
        if len(matriz)==len(matriz[i]):
            return bool(1)
        elif len(matriz)==0:
            return bool(1)
        else:
            return bool(0)
        i=i+1