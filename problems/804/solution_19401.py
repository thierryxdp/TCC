def filtra_pares(a,b,c,d):
    if a//2==0:
        a=a
    else:
        a=''
    elif b//2==0:
        b=b
    else:
        b=''
    elif c//2==0:
        c=c
    else:
        c=''
    elif d//2==0:
        d=d
    else:
        d=''
    return filtra_pares(a,b,c,d)