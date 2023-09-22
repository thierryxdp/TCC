def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada. list --> bool'''
    i = 0
    
    if len(matriz) == 0:
        return True
    for item in matriz:
        if len(item) == len(matriz):
            i += 1
    if i == len(matriz):
        return True
    else:
        return False