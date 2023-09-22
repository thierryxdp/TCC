def soma_h(n):
    '''
    A função retorna um valor h com n termos 
    '''
    h = 0
    for x in range(1, n + 1):
        h += 1  / x
    return round(h, 2)