def eh_quadrada(M):
    '''
    função que identifica se uma matriz é quadrada ou não. Obs: Uma matriz vazia
    é considerada quadrada.
    list->bool
    '''
    if len(M)==len(M[0]):
        return True 
    elif M==[]:
        return True
    else:
        return False