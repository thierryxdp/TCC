def fatorial(n):
    '''Dado um número n, calcula o fatorial dele
int -> float'''
    i=1
    a=1
    while i<=n:
        a=a*(i)
        i=i+1
    return a