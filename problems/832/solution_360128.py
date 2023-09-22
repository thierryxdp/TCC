def eh_quadrada (matriz):
    '''Dada uma função retorna True se for quadrada e False
    se não for;
    list->bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False