def media_matriz(matriz):
    '''
        Dada uma matriz qualquer, calcula a média dos seus elementos.
        list -> float
    '''
    acumulador=0
    for i in matriz:
        acumulador=acumulador+sum(i)
    elem=len(matriz)*len(matriz[0])
    return round(acumulador/elem,2)