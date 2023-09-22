def fatorial(numero):
    '''calcula e retorna o fatorial do numero recebido'''
    f=list(range(1,numero+1))
    g=1
    h=f[0]
    while g<len(f):
        h=h*f[g]
        g=g+1
    return h