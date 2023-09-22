def filtra_pares(x):
    
        d = ()
        d1 = x[0]
        d2 = x[1]
        d3 = x[2]
        d4 = x[3]
        
        if d1%2 == 0:
            d = d + (d1,)
        if d2%2 == 0:
            d = d + (d2,)
        if d3%2 == 0:
            d = d + (d3,)
        if d4%2 == 0:
            d = d + (d4,)
       
    return d