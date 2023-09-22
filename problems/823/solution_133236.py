def faltante(x):
    """função que dada uma lista, retorne qual numero está faltando;list-->int"""
    a=[0]+x+[0]
    b=0
    c=list(range(len(x)+1))+[x]+[0]
    while b<=len(a):
        if c[b]!=a[b]:
            return a[b-1]+1
        b+=1