def eh_quadrada(matriz):
    '''dada uma matriz, retorna True se ela for quadrada e False caso contrário;
    list --> bool'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False