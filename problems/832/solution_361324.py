def eh_quadrada(matriz):
    '''Calcular um funcao que identifique se uma matriz é quadrada;
    list -> bool'''
    
    if len(matriz) == 0:
        return True
    
    if len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False