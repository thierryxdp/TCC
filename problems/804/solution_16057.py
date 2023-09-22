def filtra_pares(t):
    """dada uma tupla, retorna os numeros pares"""
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return (a,b,c,d)