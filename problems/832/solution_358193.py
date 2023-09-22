def eh_quadrada(matriz):
    '''retorna se uma matriz dada e quadrada
    list->bool'''
    if len(matriz)==0:
        return True 
    elif len(matriz)==len(matriz[0]):
        return True
         
    else:
        return False