def eh_quadrada(matriz):
    ''' '''
    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == [] and matriz[0] == []:
        return True
    else:
        return False