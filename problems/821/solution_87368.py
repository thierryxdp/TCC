def fatorial(n):
    '''Função que recebe um número e retorna o seu fatorial;
    int -> int'''
    x = 1
    y = 1
    while y <= n:
        x = x*y
        y=y+1
    return x