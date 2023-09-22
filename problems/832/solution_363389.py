def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada'''
    'list--> bool'
    n = len(matriz)
    m = len(matriz[0])
    if  matriz == list():
        if matriz == n:
            return True	
        else:
            return False