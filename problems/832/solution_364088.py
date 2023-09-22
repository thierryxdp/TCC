def eh_quadrada(M):
    '''
    função que identifica se uma matriz é quadrada ou não. Obs: Uma matriz vazia
    é considerada quadrada.
    list->bool
    '''
    if M==[]:
        return True 
    elif len(M)==len(M[0]):
        return True
    else:
        return False