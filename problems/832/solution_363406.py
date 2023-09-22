def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada'''
    'list--> bool'
    n = len(matriz)
    m = len(matriz[0])
    if  m == 0:
        return True