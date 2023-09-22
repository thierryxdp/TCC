def soma_h(n):
    '''Calcula h, seguindo a formula
    int -> float
    '''
    r = 0
    for x in range(1, n+1):
        r += 1 / x
    return round(x, 2)