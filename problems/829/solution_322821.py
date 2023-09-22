def soma_h(n):
    '''Retorna h=1+1/2+1/3+...+1/n, dado o n.
    int->float'''
    h=0
    for x in range(1,n+1):
        h = h + 1/x
    return round(h,2)