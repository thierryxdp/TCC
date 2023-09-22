def eh_quadrada(M):
    '''determina se uma matriz é quadrada ou não;
    list->bool'''
    if len(M)==0:
        return True
    if len(M)==len(M[0]):
        return True
    else:
        return False