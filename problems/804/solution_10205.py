def filtra_pares(a,b,c,d,):
    tup=()
    if a%2==0:
        tup= tup+(a,)
    if b%2==0:
        tup= tup+(a,b)
    if c%2==0:
        tup= tup+(a,b,c)
    if d%2==0:
        tup= tup+(a,b,c,d)
    return tup