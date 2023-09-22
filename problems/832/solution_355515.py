def eh_quadrada(matriz):
    '''Função que, dada uma matriz, diz se ela é quadrada ou não.
    list --> bool'''
    if len(matriz) > 0:
        if len(matriz) == len(matriz[list.index(matriz,x)]):
            return True
        else:
            return False
    else:
        return True