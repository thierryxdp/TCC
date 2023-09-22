def fatorial(n):
    '''calcula o fatorial de um dado numero n; int->int'''
    i=1
    f=1
    while i<=n:
        f=f*i
        i=i+1
    return f