def filtra_pares(tup):
    '''tuple(int,int,int,int) -> tuple'''
    x=()
    if tup[0]%2==0:
        return x+(tup[0],)
    if tup[1]%2==0:
        return x+(tup[1],)
    if tup[2]%2==0:
        return x+(tup[2],)
    if tup[3]%2==0:
        return x+(tup[3])