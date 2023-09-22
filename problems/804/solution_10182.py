def filtra_pares(a,b,c,d):
    tup=()
    if a%2==0:
        tup= tup+(a,)
    if b%2==0:
        tup= tup+(b,)
    if c%2==0:
        tup= tup+(c,)
    if d%2==0:
        tup= tup+(d,)
    return a,b,c,d or a,b,c or a,b,d or a,c,d or a,b or a,c or a,d or a, or b,c,d or b,c or b,d or b, or c,d or c,