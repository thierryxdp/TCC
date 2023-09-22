def filtra_pares(tupla):
    
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    
    if a%2==0:
        return (a)
    if b%2==0:
        return (b)
    if c%2==0:
        return (c)
    if d%2==0:
        return (d,)
    else:
        return ()