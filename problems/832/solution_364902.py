def eh_quadrada(matriz):
    '''Função que recebe uma matriz e determina se ela é quadrada ou não
    
    list->bool'''
    
    if matriz == []:
        return True
    
    if len(matriz[0]) == len(matriz):
           return True
    else:
           return False