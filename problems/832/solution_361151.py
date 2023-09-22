def eh_quadrada(matriz):
    '''identifica se a matriz(matriz) fornecida é quadrada; list -> bool'''
    if len(matriz) == len(matriz[0]):
        return true 
    elif len(matriz) == 0 and len(matriz[0]) == 0:
        return true 
    else:
        return false