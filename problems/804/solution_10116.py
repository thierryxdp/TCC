def filtra_pares((a,b,c,d)):
    '''tupla -> tupla'''
    tup=()
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        tup= tup+(a,b,c,d)
    if a%2==0 and b%2==0 and c%2==0 and d%2==1:
        tup= tup+(a,b,c)
    if a%2==0 and b%2==0 and c%2==1 and d%2==0:
        tup= tup+(a,b,d)
    if a%2==0 and b%2==1 and c%2==0 and d%2==0:
        tup= tup+(a,c,d)
    if a%2==1 and b%2==0 and c%2==0 and d%2==0:
        tup= tup+(c,b,d)
    if a%2==0 and b%2==0 and c%2==1 and d%2==1:
        tup= tup+(a,b)
    if a%2==0 and b%2==1 and c%2==0 and d%2==1:
        tup= tup+(a,c)
    if a%2==1 and b%2==0 and c%2==0 and d%2==1:
        tup= tup+(b,c)
    if a%2==0 and b%2==1 and c%2==1 and d%2==0:
        tup= tup+(a,d)
    if a%2==1 and b%2==0 and c%2==1 and d%2==0:
        tup= tup+(b,d)
    if a%2==1 and b%2==1 and c%2==0 and d%2==0:
        tup= tup+(c,d)
    if a%2==0 and b%2==1 and c%2==1 and d%2==1:
        tup= tup+(a,)
    if a%2==1 and b%2==0 and c%2==1 and d%2==1:
        tup= tup+(b,)
    if a%2==1 and b%2==1 and c%2==0 and d%2==1:
        tup= tup+(c,)
    if a%2==1 and b%2==1 and c%2==1 and d%2==0:
        tup= tup+(d,)
    if a%2==1 and b%2==1 and c%2==1 and d%2==1:
        tup= tup+()
    return tup