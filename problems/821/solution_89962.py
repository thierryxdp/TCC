def fatorial(n):
    '''Função que dado um número n qualquer retorne seu
    fatorial.
    int ->int'''
    i=1
    p=1
    while i<=n:
        p=i*p
        i=i+1
    return p