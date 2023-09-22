def filtra_pares(a,b,c,d):
    if a//2==0:
        a=a
    else:
        del(a)
    if b//2==0:
        b=b
    else:
        del(b)
    if c//2==0:
        c=c
    else:
        del(c)
    if d//2==0:
        d=d
    else:
        del(d)
    return filtra_pares(a,b,c,d)