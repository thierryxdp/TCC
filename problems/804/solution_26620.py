def filtra_pares (tup):
    x=()
    if tup[0]%2==0:
        x= x +(tup[0],)
    if tup[1]%2==0:
        x=x+(tup[1],)
    if tup[2]%2==0:
        x=x+(tup[2],)
    if tup[3]%2==0:
        x=x+(tup[3],)
    return x