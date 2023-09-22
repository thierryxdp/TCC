def filtra_pares([a,b,c,d]):
    '''Função que retorna apenas os elementos pares da tupla que contém os inteiros a,b,c,d.
    tupla(int,int,int,int)->tupla'''
    if(a/2==a//2):
        a=(a,)
    else:
        a=0
    if(b/2==b//2):
        b=(b,)
    else:
        b=0
    if(c/2==c//2):
        c=(c,)
    else:
        c=0
    if(d/2==d//2):
        d=(d,)
    else:
        d=0
    return a+b+c+d