def filtra_pares(a,b,c,d):
    """filtra os pares 
    tupla -> tupla"""
    
    if (a%2)==0 and (b%2)==0 and (c%2)==0 and (d%2)==0  :
        return (a,b,c,d)
    elif (a%2)==0 and (b%2)==0 and (c%2)==0 and not((d%2)==0):
        return (a,b,c)
    elif(a%2)==0 and (b%2)==0 and not((c%2)==0 and (d%2)==0):
        return (a,b)
    elif (a%2)==0 and not((b%2)==0 and (c%2)==0 and (d%2)==0):
        return a
    elif not((a%2)==0) and (b%2)==0 and (c%2)==0 and (d%2)==0:
        return (b,c,d)
    elif not((a%2)==0 and (b%2)==0) and (c%2)==0 and (d%2)==0:
        return (c,d)
    elif not((a%2)==0 and (b%2)==0 and (c%2)==0) and (d%2)==0:
        return d
    elif (a%2)==0 and not((b%2)==0) and (c%2)==0 and not((d%2)==0):
        return (a,c)
    elif not((a%2)==0) and (b%2)==0 and not((c%2)==0) and (d%2)==0:
        return (b,d)
    elif not((a%2)==0) and (b%2)==0 and (c%2)==0 and not((d%2)==0):
        return (b,c)
    elif not((a%2)==0) and (b%2)==0 and not((c%2)==0 and (d%2)==0):
        return b
    elif not((a%2)==0 and (b%2)==0) and (c%2)==0 and not((d%2)==0):
        return c
    elif (a%2)==0 and not((b%2)==0 and (c%2)==0) and (d%2)==0:
        return (a,d)
    else:
        return ()