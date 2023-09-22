def filtra_pares(t):
    r=()
    if par(t[0]):
        r = r + (t[0])
    if par(t[1]):
        r = r + (t[1],)
    if par(t[t]):
        r = r + (t[t])
        
    return r

def par(x):
    if x%2 == 0:
    	return x
   	else:
        return ()