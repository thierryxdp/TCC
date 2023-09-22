def filtra_pares (x):
    
    """...
    """
    xv = ()
    if x[0]%2 == 0:
        xv = xv + (x[0],)
    if x[1]%2 == 0:
        xv = xv + (x[1],)
    if x[2]%2 == 0:
        xv = xv + (x[2],)
    if x[3]%2 == 0:
        xv = xv + (x[3])
    return xv