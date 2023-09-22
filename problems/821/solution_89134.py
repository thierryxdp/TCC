def fatorial(n):
    '''Dado um numero, retorna o fatorial do mesmo.int->int'''
    a=1
    b=n
    while a<n:
        b=b*(n-a)
        a=a+1
    return b