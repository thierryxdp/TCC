def filtra_pates(x):
    ''' '''
    a,b,c,d = x
    
    
    if (a/2) == (a//2):
        y = a
    if (b/2) == (b//2):
        y = (y,b)
    if (c/2) == (c//2):
        y = (y,c)
    if (d/2) == (d//2):
        y = (y,d)
    return y