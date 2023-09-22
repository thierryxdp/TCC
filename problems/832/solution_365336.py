def eh_quadrada(matriz):
    ''' funcao que diz se a matriz é quadrada. list --> bool'''
    
    if len(matriz) == 0:
        return True
    for linhas in matriz:
        if len(matriz) == len(matriz[0]):
            return True
    else:
        return False