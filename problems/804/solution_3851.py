def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    v=()
    
    if a%2==0:
        v=v+(a,)
    
    if b%2==0:
        v=v+(b,)
    
    if c%2==0:
        v=v+(c,)
    
    if d%2==0:
        v=v+(d,)
    return v