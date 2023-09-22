#Start your python function here
def filtra_pares(a,b,c,d):
    '''Dado uma tupla com quatro inteiros a,b,c e d, retorne somente os números pares;
    int,int,int,int -> int,...'''
    t=(a,b,c,d)
    if a%2==0:
        return a
        if b%2==0:
            return a,b
            if c%2==0:
                return a,b,c
                if d%2==0:
                    return a,b,c,d
    elif b%2==0:
        return b
        if c%2==0:
            return b,c
        if d%2==0:
            return b,c,d
    elif c%2==0:
        return c
        if d%2==0:
            return c,d
    elif d%2==0:
        return d
    else:
        return