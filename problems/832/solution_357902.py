def eh_quadrada(A):
    '''Funcao que identifica se a matriz e quadrada'''
    '''list -> bool'''
    A = []
    if len(A) == len(A[0]):
        return True
    else:
        return False