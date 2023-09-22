def fatorial(n):
    '''calcula o fatorial de n, int->int'''
    i=n
    while i>=1:
        i=i-1
        n=n*i
    return n