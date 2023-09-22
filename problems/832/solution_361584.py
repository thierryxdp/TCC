def eh_quadrada(matriz:int)->bool:
    '''diz se a matriz é quadrda'''
    for i in matriz:
        if len(matriz) != len(i):
            return False
    return True