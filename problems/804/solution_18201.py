def filtra_pares(tupla):
    
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    
    if a%2==0:
        a=(a,)
    if b%2==1:
        b=(b,)
    if c%2==1:
        c=(c,)
    if d%2==1:
        d=(d,)
    return tupla