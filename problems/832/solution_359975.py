def eh_quadrada(m):
    '''é quad.'''
    if len(m) * len(m[0])==0:
        return True
    if len(m) != len(m[0]):
        return False
    if len(m) == len(m[0]):
        return True