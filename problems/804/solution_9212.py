def filtra_pares(par):
    x = par[0]
    y = par[1]
    z = par[2]
    w = par[3]
    pares = ()
    if x%2==0:
        pares=pares+(x,)
    if y%2==0:
        pares=pares+(y,)
    if z%2==0:
        pares=pares+(z,)
    if w%2==0:
        pares=pares+(w,)
    return pares