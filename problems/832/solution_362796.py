def eh_quadrada (matriz:list)->bool:
    '''Ientifica se a matriz é quarada'''
    for i in matriz:
        if len(matriz) != len(i):
            return False 
    return True