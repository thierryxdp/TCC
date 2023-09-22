def filtra_pares(tup):
    x1=tup[0]%2
    x2=tup[1]%2
    x3=tup[2]%2
    x4=tup[3]%2
    z=()
    if x1==0:
        z=z+(tup[0],)
    if x2==0:
        z=z+(tup[1],)
    if x3==0:
        z=z+(tup[2],)
    if x4==0:
        z=z+(tup[3],)
        else:
            return z
        return z