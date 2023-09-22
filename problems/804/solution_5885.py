def filtra_pares([a,b,c,d]):
    t1=a%2
    t2=b%2
    t3=c%2
    t4=d52
    if t1==0 and t2==0 and t3==0 and t4==0:
        return (t1,t2,t3,t4)
    elif t1!=0 and t2==0 and t3==0 and t4==0:
        return (t2,t3,t4)
    elif t1==0 and t2!=0 and t3==0 and t4==0:
        return (t1,t3,t4)
    elif t1==0 and t2==0 and t3!=0 and t4==0:
        return (t1,t2,t4)
    elif t1==0 and t2==0 and t3==0 and t4!=0:
        return(t1,t2,t3)
    else:
        return ()