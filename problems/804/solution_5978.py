def filtra_pares(tupla):
    tupla[0]=a
    tupla[1]=b
    tupla[2]=c
    tupla[3]=d
    if a%2==1:
        return (b,c,d)
    if b%2==1:
        return(a,c,d)
    if c%2==1:
        return(a,b,d)
    if d%2==1:
        return(a,b,c)