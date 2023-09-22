def fatorial(n):
    ''' Função que calcula o fatorial de um numero n.
    int->int'''
    l=list(range(1,n+1))
    i=0
    s=1
    d=len(l)
    while(i<d):
        s = s*l[i]
        i=i+1
    return s