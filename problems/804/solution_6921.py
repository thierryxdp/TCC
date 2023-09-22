def filtra_pares(tt):
    
    par = ()
    a= tt[0]
    b= tt[1]
    c= tt[2]
    d= tt[3]
    
    if a%2 == 0:
        par = par + (a,) 
    if b%2 == 0:
        par = par + (b,) 
    if c%2 == 0:
        par = par + (c,)
    if d%2 == 0:
        par = par + (d,)
    
    return par