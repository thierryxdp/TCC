def qtd_divisores (n, l):
    '''conta quantos divisores tem o numero'''
    n = ('numero:')
    for i in range(l,n):
        if n % i == 0:
            return (i)