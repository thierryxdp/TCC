def filtra_pares(a,b,c,d):
    """retorna uma tupla só dos valores pares da tupla inicial."""
    if (a%2==0):
        if (b%2==0):
            if (c%2==0):
                if (d%2==0):
                    return (a,b,c,d)
                else:
                    return (a,b,c)
            else:
                if (d%2==0):
                    return (a,b,d)
                else:
                    return (a,b)
        else:
            if (c%2==0):
                if(d%2==0):
                    return (a,c,d)
                else(a,c)
            else:
                return (a)
else:
    if (b%2==0):
        if (c%2==0):
            if (d%2==0):
                return (b,c,d)
            else:
                return (b,c)
        else:
            if (d%2==0):
                return (b,d)
            else(b)
    else:
        if (c%2==0):
            if (d%2==0):
                return (c,d)
            else:
                return (c)
        else:
            if (d%2==0):
                return(d)