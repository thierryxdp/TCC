def eh_quadrada(m):
    '''é quad.'''
    if len(m) == len(m[0]):
        return True
    elif len(m) != len(m[0]):
        return False
    elif len(m) and len(m[0]) == 0:
        return True