def eh_quadrada(M):
    '''
    retorna, em booleano, se uma matriz é quadrada ou não
    list -> bool
    '''
    vazia = []
    if len(M)==len(M[0]):
        return True
    elif M==vazia:
        return True
    else:
        return False