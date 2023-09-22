def resto(a, b):
    return a % b

def par(n):
    return resto(n, 2) == 0

def filtra_pares(t):
    ret = ()
    if par(t[0]):
        ret = ret + (t[0], )
    if par(t[1]):
    	ret = ret + (t[1], )
    if par(t[2]):
        ret = ret + (t[2], )
    if par(t[3]):
        ret = ret + (t[3], )
	if par(t[4]):
        ret = ret + (t[4], )
    return ret