def filtra_pares(n1,n2,n3,n4):
    (n1,n2,n3,n4)[0:1]==a
    (n1,n2,n3,n4)[1:2]==b
    (n1,n2,n3,n4)[2:3]==c
    (n1,n2,n3,n4)[3:4]==d
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0 and b%2==0 and c%2==0:
        return(a,b,c)
    elif a%2==0 and b%2==0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2==0 and b%2==0:
        return(a,b)
    elif a%2==0 and c%2==0:
        return(a,c)
    elif a%2==0 and d%2==0:
        return(a,d)
    elif b%2==0 and c%2==0:
        return(b,c)
    elif b%2==0 and d%2==0:
        return(b,d)
    elif c%2==0 and d%2==0:
        return(c,d)
    elif a%2==0:
        return (a,)
    elif b%2==0:
        return (b,)
    elif c%2==0:
        return (c,)
    else:
        return(d,)