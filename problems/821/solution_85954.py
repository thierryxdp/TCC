def fatorial(n):
    '''Retorna o fatorial de n;
    int -> int'''
    f=n
    while n-1!=0:
        f=f*(n-1)
        n=n-1
    return f