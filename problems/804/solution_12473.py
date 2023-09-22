def filtra_pares(a,b,c,d):
    x=[]
    if (a[0]%2)==0:
        x= x+(a)
    if (b[1]%2)==0:
        x= x+(b)
    if (c[2]%2)==0:
        x= x+(c)
    if (d[3]%2)==0:
        x= x+(d)
    return x