def filtra_pares(a,b,c,d):
    x=a%2==0
    y=b%2==0
    z=c%2==0
    w=d%2==0
    if x and y and z and w:
        return (a,b,c,d)