def fatorial(n):
    '''calcula o fatorial de um numero.
    int->int'''
    fatorial=0
    while n>0:
        fatorial=n*(n-1)
        n-=1
        
    return fatorial