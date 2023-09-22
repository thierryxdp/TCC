def fatorial(n):
    '''retorna o fatorial de n
    int->int'''
    i=1
    f=1
    while i<=n:
        f*= i
        i=i+1
    return f