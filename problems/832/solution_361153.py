def eh_quadrada(matriz):
    '''identifica se a matriz(matriz) fornecida é quadrada; list -> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True 
    else:
        return False