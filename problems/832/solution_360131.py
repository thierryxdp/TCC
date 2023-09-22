def eh_quadrada(M):
    '''
    list --- > boolean
    '''
    if M == []:
        return True
    elif len(M) == len(M[0]):
        return True
    else:
        return False