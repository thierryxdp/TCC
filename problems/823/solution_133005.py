def faltante(x):
    '''Retorna o número da peça faltante.
    list -> int'''
    i=2
    a=1
    x=x.sort()
    while i<len(x):
        if x[i]==x[a]+1:
            i=i+1
            a=a+1
        else:
            return i