def eh_quadrada(M):
    '''
    list --- > boolean
    retorna True se matriz passada é quadrada,
    retorna False se não
    '''
    if M == []:
        return True
    elif len(M) == len(M[0]):
        return True
    else:
        return False