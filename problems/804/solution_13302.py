def filtra_pares(tupla):
    (a,b,c,d)=tupla
    pares=()
    if (a%2==0):
        pares=pares+ (a,)
    if (b%2==0):
        pares=pares+ (b,)
    if (c%2==0):
        pares=pares+ (c,)
    if (d%2==0):
        pares= pares+ (d,)
        return pares