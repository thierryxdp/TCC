def eh_quadrada(M):
    '''
	função que identifica se uma matriz é quadrada;
    list -> bool
    '''
    if len(M) == len(M[0]):
        return True
    else:
        return False