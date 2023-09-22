def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    if a%2==1:
        return (b,c,d)
    else:
        return (a,b) or (a,c) or (a,d)
    if b%2==1:
        return(a,c,d)
    if c%2==1:
        return(a,b,d)
    if d%2==1:
        return(a,b,c)