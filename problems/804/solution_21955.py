def par(j):
    return j%2 == 0
    
def filtra_pares(v):
    r = ()
    if par(v[0]):
        r = r + (v[0],)
    if par(v[1]):
    	r = r + (v[1],)
    if par(v[2]):
    	r = r + (v[2],)
    if par(v[3]):
    	r = r + (v[3],)
    return r