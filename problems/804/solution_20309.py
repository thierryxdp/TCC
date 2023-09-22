def filtra_pares(m,n,o,p):
    """retorna uma tupla que tenha os elementos pares da original na mesma ordem que em que estava
    int, int, int, int -> int"""
    if m%2==0 and n%2==0:
        return m,n
    elif m%2==0 and o%2==0:
        return m,o
    elif n%2==0 and o%2==0:
        return n,o
    elif m%2==0 and p%2==0:
        return m,p
    elif n%2==0 and p%2==0:
        return n,p
    elif o%2==0 and p%2==0:
        return o,p
    else:
        return m%2==0,n%2==0,o%2==0,p%2==0