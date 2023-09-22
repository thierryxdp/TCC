def filtra_pares(x=(0,1,2,3)):
    '''tuple(int,int,int,int) -> tupla'''
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    tup=()
    if (int(a)%2)==0:
        tup= tup+(a,)
    if (int(b)%2)==0:
        tup= tup+(b,)
    if (int(c)%2)==0:
        tup= tup+(c,)
    if (int(d)%2)==0:
        tup= tup+(d,)
    return tup