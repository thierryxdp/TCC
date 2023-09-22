def eh_quadrada(matriz):
    '''Dada uma matriz qualquer, retorna se ela é quadrada ou não. list->bool'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False