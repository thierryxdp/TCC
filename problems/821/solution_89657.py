def fatorial(n):
    '''retorna o fatorial de n.
    int->int'''
    x=1
    while n!=1:
        x=n*x
        n=n-1     
    return x