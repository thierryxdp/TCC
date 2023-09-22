def eh_quadrada(matriz):
    '''Função que, dada uma matriz, diz se ela é quadrada ou não.
    list --> bool'''
    for x in matriz:
        if len(matriz) == len(matriz[x]):
            return True
        else:
            return False