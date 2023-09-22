def fatorial(n):
    '''função que dado um número, retorne o seu fatorial'''
    if n<=1:
        return 1
    return n*fatorial(n-1)