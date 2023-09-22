def eh_quadrada (matriz):
    '''Dada uma função retorna True se for quadrada e False
    se não for;
    list->bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == []:
        return True
    else:
        return False