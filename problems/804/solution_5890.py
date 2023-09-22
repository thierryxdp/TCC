def filtra_pares(tuple=(a,b,c,d)):
    t1=a%2
    t2=b%2
    t3=c%2
    t4=d%2
    if t1==0 and t2==0 and t3==0 and t4==0:
        return (a,b,c,d)
    elif t1!=0 and t2==0 and t3==0 and t4==0:
        return (b,c,d)
    elif t1==0 and t2!=0 and t3==0 and t4==0:
        return (a,c,d)
    elif t1==0 and t2==0 and t3!=0 and t4==0:
        return (a,b,d)
    elif t1==0 and t2==0 and t3==0 and t4!=0:
        return(a,b,c)
    else:
        return ()