def filtra_pares(a,b,c,d):
    da=a//2
    db=b//2
    dc=c//2
    dd=d//2
    
    if da==0 and db==0 and dc==0 and dd==0:
        return (a,b,c,d)
    if da==0 and db==0 and dc==0 and dd!=0:
        return (a,b,c)
    if da==0 and db==0 and dc!=0 and dd!=0:
        return (a,b)
    if da==0 and db!=0 and dc!=0 and dd!=0:
        return (a,)
    if da!=0 and db==0 and dc==0 and dd==0:
        return (b,c,d)
    if da!=0 and db==0 and dc==0 and dd!=0:
        return (b,c)
    if da!=0 and db==0 and dc!=0 and dd!=0:
        return (b,)
    if da!=0 and db!=0 and dc==0 and dd==0:
        return (c,d)
    if da!=0 and db!=0 and dc==0 and dd!=0:
        return (c,)
    if da!=0 and db!=0 and dc!=0 and dd==0:
        return (d,)