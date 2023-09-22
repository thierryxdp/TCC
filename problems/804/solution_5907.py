tuple=(a,b,c,d)
def filtra_pares(tuple):
    t1=int(a)%2
    t2=int(b)%2
    t3=int(c)%2
    t4=int(d)%2
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