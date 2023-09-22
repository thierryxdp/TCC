def filtra_pares(a, b, c, d):
    '''Função para determinar os ementos pares'''
    t1 = (a,b,c,d)
    x = list(t1)
    
    a = max(x[::2])
    b = max(x[::2])
    c = max(x[::2])
    d = max(x[::2])

    y = (a,b,c,d)

    if  a > b:
        return y
    else:
        return ()