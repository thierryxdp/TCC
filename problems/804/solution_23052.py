def filtra_pares(a,b,c,d):
    r=()
    if par(t[0]):
        r = r + (t[0])
    if par(t[1]):
        r = r + (t[1],)
    if par(t[2]):
        r = r + (t[2])
    if par(t[3]):
        r = r + (t[3])
    else: 
        return ()
    return r

def par(x):
    if x%2 == 0:
    	return x