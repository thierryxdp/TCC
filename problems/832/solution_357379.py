def eh_quadrada(matriz):
    '''Retorna True se a matriz é quadrada. Retorna
    False se não for quadrada;
    list -> boolean'''
    
    if matriz == []:
        return True
    
    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False