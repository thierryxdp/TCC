def fatorial(n):
    'Calcula o fatorial de um número.'
    c=1
    i=1
    while i<=n:
        c*=i
        i+=1
    return c