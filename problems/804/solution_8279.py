def filtra_pares (a,b,c,d):
    pares=()
    if a%2==0:
        pares += (a,)        
    if b%2==0:
        pares += (b,)
    if c%2==0:
        pares += (c,)
    if d%2==0:
        pares += (d,)
    return pares