def eh_quadrada(matriz):
    '''Dada uma matriz verifica se ela é ou não quadrada retorando um booleano
    list -> bool'''
    
    if len(matriz) == 0 or len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False