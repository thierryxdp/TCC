def qnt_divisores(n):
    '''Dado um numero n, retorna a quantidade de divisores que esse numero tem.
    int -> int'''
    contador=0
    for div in (0,n):
        if n%div==0:
            yield div
        yield div