def fatorial(n):
    '''retorna o fatorial do numero n; int->int'''
    fat=(n-1)
    contador=0
    f=1
    
    while fat!=1:
        f=fat*f
        fat=(fat-1)
    if n=1:
        return 1
    return f*n