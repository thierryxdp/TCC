def filtra_pares(tuplaIn):
    par = ()
    if tuplaIn[0]%2 == 0:
        par = par + (a,) 
    if tuplaIn[1]%2 == 0:
        par = par + (b,) 
    if tuplaIn[2]%2 == 0:
        par = par + (c,)
    if tuplaIn[3]%2 == 0:
        par = par + (d,)
    
    return par