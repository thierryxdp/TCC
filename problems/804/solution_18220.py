def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]

    
    if (a%2==1):
        a=()
    if (b%2==1):
        b=()
    if (c%2==1): 
        c=()
    if (d%2==1):
        d=()
    else:
        tupla=(a,b,c,d)
    
    return (a,b,c,d)