def filtra_pares(p):
    """..."""
    t=()
    x=par(p[0])
    y=par(p[1])
    z=par(p[2])
    w=par(p[3])
    
    def par(n):
        if n%2 == 0:
            return n
        else:
            return
        
    if x%2 == 0:
        t+=x
    if y%2 == 0:
        t+=y
    if z%2 == 0:
        t+=z
    if w%2 == 0:
        t+=w
    return t