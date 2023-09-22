def eh_quadrada(m):
    '''é quad.'''
    if len(m) != len(m[0]):
        return False
    if len(m) == len(m[0]):
        return True
    if m ==0:
        return True