def faltante(x):
    '''Retorna o número da peça faltante.
    list -> int'''
    i=2
    a=1
    x==x.sort()
    u=len(x)-1
    while i<1000:
        if x[a]==len(x)-1:
            return x[u]+1
        elif x[i]==x[a]+1:
            i=i+1
            a=a+1
        else:
            return i