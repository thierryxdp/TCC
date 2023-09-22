def eh_quadrada(M):
    '''
    retorna, em booleano, se uma matriz é quadrada ou não
    list -> bool
    '''
    vazia=0
    if len(M)==len(M[0]) or len(M)==vazia:
        return True
    else:
        return False