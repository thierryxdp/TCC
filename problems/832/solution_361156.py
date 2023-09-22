def eh_quadrada(m):
    '''Retorna se é matriz quadrada'''
    l = len(m)
    for n in m:
        if len(n) != l:
            return False
    else:
        return True