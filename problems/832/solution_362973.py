def eh_quadrada (matriz:list)->bool:
    '''Identifica se a matriz é quadrada'''
    for i in matriz:
        if len(matriz) != len(i):
            return False 
    return True