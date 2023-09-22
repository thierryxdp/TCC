def filtra_pares(a,b,c,d):
    """função que recebe 4 elementos de uma tupla e retorna
    uma nova tupla apenas com os elementos pares
    tupla -> tupla"""
    t=(a,b,c,d)
    nova=()
    if(a%2==0):
        nova=a
    else:
        a=()
    if(b%2==0):
        nova=a,b
    else:
        b=()
    if(c%2==0):
        nova=a,b,c
    else:
        c=()
    if(d%2==0):
        nova=a,b,c,d
    else:
        d=()
    return nova