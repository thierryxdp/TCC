def filtra_pares([a,b,c,d]):
    x=[]
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return tuple(a,b,c,d)