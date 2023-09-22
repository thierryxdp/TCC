def eh_quadrada(m):
    '''Recebe uma matriz em formato de lista e retorna True
    se ela for quadrada e False se nao for'''
    if m==[]:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False