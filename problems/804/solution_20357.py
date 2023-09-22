def filtra_pares(a,b,c,d):
    da=a%2
    db=b%2
    dc=c%2
    dd=d%2
    if da==0:
        tupla=()+(a,)
    if db==0:
        tupla=()+(b,)
    if dc==0:
        tupla=()+(c,)
    if dd==0:
        tupla=()+(d,)
    return tupla