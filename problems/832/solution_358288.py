def eh_quadrada(matriz):
    '''Identifica se uma matriz possui o mesmo número de linhas e colunas
    list -> bool'''
    
    if matriz == []:
        return True
    
    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False