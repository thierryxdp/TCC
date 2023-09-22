def filtra_pares(a,b,c,d):
    if a//2==0:
        a=a
    else:
        a=''
    if b//2==0:
        b=b
    else:
        b=''
    if c//2==0:
        c=c
    else:
        c=''
    if d//2==0:
        d=d
    else:
        d=''
    return filtra_pares(a,b,c,d)