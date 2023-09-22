def eh_quadrada(matriz):
    '''Dada uma matriz, retorna se a matriz é quadrada ou não
    list->bool'''
    
    lin=len(matriz)
    col=len(matriz[0])
    
    if lin == 0:
        return True
    if lin == col:
        return True 
    if lin != col:
        return False