def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada'''
    'list--> bool'
    
    if  matriz==list():
        return True
    else:
        n = len(matriz)
        m = len(matriz[0])
        return m == n