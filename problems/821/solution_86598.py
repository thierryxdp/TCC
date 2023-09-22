def fatorial(n):
    '''calcula o fatorial do inteiro n
    int->int'''
    i=1
    fatorial=n
    while i<n:
        fatorial=fatorial*i
        i+=1
    return fatorial