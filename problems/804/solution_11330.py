def filtra_pares(x):
    '''tuple(int,int,int,int) -> tupla'''
    a,b,c,d=x
    tup=()
    if (int(a)%2)==0:
        tup= tup+(a,)
    if (int(b)%2)==0:
        tup= tup+(b,)
    if (int(c)%2)==0:
        tup= tup+(c,)
    if (int(d)%2)==0:
        tup= tup+(d,)
    return tup#Start your python function here