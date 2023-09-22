def filtra_pares(p):
    """..."""
    t=()
    x=p[0]
    y=p[1]
    z=p[2]
    w=p[3]
        
    if x%2 == 0:
        t+=str(x)
    if y%2 == 0:
        t+=str(y)
    if z%2 == 0:
        t+=str(z)
    if w%2 == 0:
        t+=str(w)
    return t