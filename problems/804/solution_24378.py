def filtra_pares(a,b,c,d):
    """Funçao que recebe uma tupla com quatro elementos inteiros como parametro
    e retorna uma nova tupla apenas com os elementos pares da original. """
    tupla=(a,b,c,d)
    if a%2==0:
        return(a)
    elif b%2==0:
        return(b)
    elif c%2==0:
        return(c)
    elif d%2==0:
        return(d)
    else:
        return(a,b,c,d)