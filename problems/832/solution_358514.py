def eh_quadrada(matriz):
    '''retorna se a matriz do arg e quadrada ou nao
    list(list) -> bool'''
    
    if len(matriz) == len(matriz[0]):
        return True
    
    elif len(matriz) == 0:
        return True
    
    else:
        return False