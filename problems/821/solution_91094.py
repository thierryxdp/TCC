def fatorial(n):
    '''calcula o fatorial de um numero'''
    f=1
    i=0
    while n >= 1:
        f = f*i
        i += 1
    return f