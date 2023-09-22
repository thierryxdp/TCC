def filtra_pares(a,b,c,d):
    '''retorna uma tupla com os numeros pares de entrada
    int,int,int-->tupla'''
    e=a%2
    f=b%2
    g=c%2
    h=d%2
    if e==0:
        if f==0:
            if g==0:
                if h==0:
                    return (a,b,c,d)
    if f==0:
        if g==0:
            if h==0:
                return (b,c,d)
    if g==0:
        if h==0:
            return (c,d)
    if h==0:
        return (d)