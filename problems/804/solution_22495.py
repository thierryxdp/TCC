def filtra_pares(x,y,z,w):
    
    d =()
    
    if x%2 == 0:
        d = d + (x,)
    if y%2 ==0:
        d = d + (y,)
    if z%2 == 0:
        d = d + (z,)
    if w%2 == 0:
        d = d + (w,)
        
        return d