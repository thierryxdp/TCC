def filtra_pares(a,b,c,d):
    """Calacula e retorna uma nova tupla com numeros pares de uma tupla original"""
    if (a<0) % 2==0:
        return a
    if (a>0) % 2==0:
        return -a
    if (b<0) % 2==0:
        return b
    if (b>0) % 2==0:
        return -b
    if (c<0) % 2==0:
        return c
    if (c>0) % 2==0:
        return -c
    if (d<0) % 2==0:
        return d
    if (d>0) % 2==0:
        return -d
    if a,b,c,d % 2==0:
        return a, b, c, d
    else:
        return 0