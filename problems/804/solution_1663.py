def filtra_pares(tup):
vazia=(,)
    if tup[0]%2==0:
         vazia=vazia+(tup[0],)
    if tup[1]%2==0:
         vazia=vazia+(tup[1],)
    if tup[2]%2==0:
         vazia=vazia+(tup[2],)
    if tup[3]%2==0:
         vazia=vazia+(tup[3],)
    return vazia