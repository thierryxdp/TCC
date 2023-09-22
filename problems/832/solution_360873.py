def eh_quadrada(matriz):
    '''Retorna se uma matriz é quadrada ou não;list->bool'''
    A=[]
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False