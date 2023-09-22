def fatorial(n):
    '''função que a partir de um número inteiro retorna o seu fatorial;int->int'''
    r=1
    while (n-1)!=0:
        r=r*n
        n=n-1
    return r