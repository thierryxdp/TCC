def filtra_pares(x,y,z,q,):
    """Função que filtra os números pares de uma tupla com 4 elementos"""
    if x%2==0 and y%2==0 and z%2==0 and q%2==0:
        return(x,y,z,q,)
    elif x%2==0 and y%2==0 and z%2==0:
        return (x,y,z,)
    elif x%2==0 and y%2==0:
        return (x,y,)
    elif y%2==0 and z%2==0 and q%2==0:
        return(y,z,q,)
    elif y%2==0 and z%2==0:
        return(y,z,)
    elif y%2==0:
        return(y,)
    elif z%2==0 and q%2==0:
        return(z,q,)
    elif z%2==0:
        return(z,)
    elif q%2==0:
        return (q,)
    else:
        return ('',)