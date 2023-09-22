def filtra_pares(a,b,c,d):
    tup = ()
    tup2= ()
    tup3= ()
    tup4= ()
    if a%2 == 0:
        tup = (a,)
    else:
        tup = ()
    if b%2 == 0:
        tup2 = (b,)
    else:
        tup2 = ()
    if c%2 == 0:
        tup3 = (c,)
    else:
        tup3 = ()
    if d%2 == 0:
        tup4 =(d,)
    else:
        tup3 = ()
    return tup + tup2 + tup3 + tup4 
    

    

    
 
    

    
    #Start your python function here