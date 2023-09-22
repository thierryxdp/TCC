def filtra_pares(a,b,c,d):
    e,f,g,h=a%2,b%2,c%2,d%2
    if e=0 and f=0 and g=0 and h=0:
        return (a,b,c,d)
    elif e=0 and f=0 and g=0 or h!=0:
        return(a,b,c)
    elif e=0 and f=0 or g!=0 and h!=0:
        return(a,b)
    elif e=0 or f!=0 and g!=0 and h!=0:
        return (a)
    else:
        return