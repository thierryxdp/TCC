def filtra_pares(a,b,c,d):
    """Retorna uma tupla contendo apenas os elementos pares da original.
    int,int,int,int->tupla(int)"""
    if (a%2==0)and(b%2==0)and(c%2==0)and(d%2==0):
        return tuple(a,b,c,d)
    elif (a%2==0)and(b%2==0)and(c%2==0)and(d%2!=0):
        return tuple(a,b,c)
    elif (a%2==0)and(b%2==0)and(c%2!=0)and(d%2==0):
        return tuple(a,b,d)
    elif (a%2==0)and(b%2!=0)and(c%2==0)and(d%2==0):
        return tuple(a,c,d)
    elif (a%2!=0)and(b%2==0)and(c%2==0)and(d%2==0):
        return tuple(b,c,d)
    elif (a%2!=0)and(b%2!=0)and(c%2==0)and(d%2==0):
        return tuple(c,d)
    elif (a%2!=0)and(b%2==0)and(c%2!=0)and(d%2==0):
        return tuple(b,d)
    elif (a%2!=0)and(b%2==0)and(c%2==0)and(d%2!=0):
        return tuple(b,c)
    elif (a%2==0)and(b%2!=0)and(c%2==0)and(d%2!=0):
        return tuple(a,c)
    elif (a%2==0)and(b%2==0)and(c%2!=0)and(d%2!=0):
        return tuple(a,b)
    elif (a%2==0)and(b%2!=0)and(c%2!=0)and(d%2==0):
        return tuple(a,d)
    elif (a%2!=0)and(b%2!=0)and(c%2!=0)and(d%2==0):
        return tuple(d,)
    elif (a%2!=0)and(b%2!=0)and(c%2==0)and(d%2!=0):
        return tuple(c,)
    elif (a%2!=0)and(b%2==0)and(c%2!=0)and(d%2!=0):
        return tuple(b,)
    elif (a%2==0)and(b%2!=0)and(c%2!=0)and(d%2!=0):
        return tuple(a,)
    elif (a%2!=0)and(b%2!=0)and(c%2!=0)and(d%2!=0):
        return tuple(' ')