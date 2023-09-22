def eh_quadrada (matriz:list)->bool:
    '''recebe uma matriz e verifica se ela é quarada'''
    for i in matriz:
        if len(matriz) != len(i):
            return False 
    return True