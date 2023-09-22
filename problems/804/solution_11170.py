def filtra_pares(tupla):
    """recebe uma tupla com 4 valores e retorna os numeros pares dela. str->int."""
    A,B,C,D = tupla
    a = int(A)
    b = int(B)
    c = int(C)
    d = int(D)
    if (a%2==0):
        a = a
    elif not(a%2==0):
        a = ()
    if (b%2==0):
        b = b
    elif not(b%2==0):
        b = ()
    if (c%2==0):
        c = c
    elif not(c%2==0):
        c = ()
    if (d%2==0):
        d = d
    elif not(d%2==0):
        d = ()
            
    return (a,b,c,d)