def fatorial(n):
    '''calcula o fatorial de n, int->int'''
    i=n-1
    while i>=1:
        n=n*i
        i=i-1
    return n