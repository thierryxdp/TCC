def fatorial(n):
    '''faz a conta fatorial a partir deste numero'''
    a= 1
    while n >= 1:
        a=n*a
        n=n-1
    return a