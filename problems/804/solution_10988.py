def filtra_pares(a,b,c,d):
    
    nu1=a//2==0
    nu2=b//2==0
    nu3=c//2==0
    nu4=d//2==0
     if  nu1=a//2==0:
        return (a,)
     if  nu2=a//2==0:
        return (b,)
     if  nu3=a//2==0:
        return (c,) 
    if  nu4=a//2==0:
        return (d,)
    else: 
        return (a,b,c,d)