def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada'''
    'list--> bool'
    
    m = len(matriz)
    n = len(matriz[0])
    if  m != 0:
        return m==n
    else:
        matriz=list()
        return True