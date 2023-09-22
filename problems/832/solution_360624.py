def eh_quadrada (matriz):
    '''funcao que recebe uma matriz e retorna 
True se ela for quadrada e False caso contrario
list->bool'''
    if not len(matriz):
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False