def eh_quadrada(matriz):
    '''Dada uma matriz, retorna se a matriz é quadrada ou não
    list->bool'''
    
    if len(matriz) == 0:
        return True
    if len(matriz) == len(matriz[0]):
        return True 
    if len(matriz) != len(matriz[0]):
        return False