def filtra_pares(x):
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if (a%2)==0:
        return a
    elif (b%2)==0:
        return b
    elif (c%2)==0:
        return c
    elif (d%2)==0:
        return d
    else:
        if (a%2)==0 and (b%2)==0:
            return a,b
        elif (a%2)==0 and (c%2)==0:
            return a,c
        elif (a%2)==0 and (d%2)==0:
            return a,d
        elif (b%2)==0 and (c%2)==0:
            return b,c
        elif (b%2)==0 and (d%2)==0:
            return b,d
        elif (c%2)==0 and (d%2)==0:
            return c,d
        else:
            if (a%2)==0 and (b%2)==0 and (c%2)==0:
                return a,b,c
            if (a%2)==0 and (b%2)==0 and (d%2)==0:
                return a,b,d
            if (a%2)==0 and (c%2)==0 and (d%2)==0:
                return a,c,d
            if (b%2)==0 and (c%2)==0 and (d%2)==0:
                return b,c,d
            else:
                if (a%2)==0 and (b%2)==0 and (c%2)==0 and (d%2)==0:
                    return a,b,c,d
                else:
                    return (,)