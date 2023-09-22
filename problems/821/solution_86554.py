def fatorial (n):
    '''Função que recebe um numero e retorna com o seu fatorial.
    int -> int'''
    prox=1
    b=n
    while prox<n:
        b = b*(n-prox)
        prox = prox + 1
    return b