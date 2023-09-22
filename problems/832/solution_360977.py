def eh_quadrada(M):
    '''
       funcao que recebe uma matriz e identifica se ela 
       eh quadrada
       list -> bool
    '''
    if len(M) == 0:
        return True 
    elif len(M) == len(M[0]):
        return True
    else:
        return False