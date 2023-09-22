def eh_quadrada(matriz):
    '''funcao que dada uma matriz, identifica se ela eh quadrada ou não
       matriz -> boolean'''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False