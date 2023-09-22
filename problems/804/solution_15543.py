def filtra_pares(tup):
    la=()
    if(tup[0] % 2 == 0):
        la=la+(tup[0], ) 
    if(tup[1] % 2 == 0):
        la=la+(tup[1], ) 
    if(tup[2] % 2 == 0):
        la=la+(tup[2], )
    if(tup[3] % 2 == 0):
        la=la+(tup[3], )
    return la