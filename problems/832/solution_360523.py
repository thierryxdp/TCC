def eh_quadrada(matriz):
    '''Função que recebe uma matriz como entrada e
    identifica se é uma matriz quadrada, retornando
    True, ou não, retornando False. list(list)->bool'''
    if len(matriz) == 0:
        return True 
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False