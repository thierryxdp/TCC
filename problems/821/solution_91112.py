def fatorial(n):
    '''calcula o fatorial de um numero'''
    f = 1
    i = 1
    while i <=n:
        f*=i
        i+=1
    return f