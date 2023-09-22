def conta_numero(n,m):
    ''' retorna quantas vezes o número n aparece na matriz m;
    int, mat -> int'''
    x=0
    for l in m:
        x = x + list.count(l,n)
    return x